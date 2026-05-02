import requests
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.dialects.postgresql import insert
from datetime import datetime


# CONFIGURATION

DB_CONFIG = {
    "user": "postgres",
    "password": "mysecretpassword",
    "host": "localhost",
    "port": "5432",
    "dbname": "dgbet_db"
}

# Official Graph Endpoint
GRAPHQL_URL = "https://thegraph.onchainfeed.org/subgraphs/name/azuro-protocol/azuro-api-polygon-v3"


# 1. EXTRACT

def extract_data():
    """Fetches bet data from the GraphQL API."""
    print("--- Step 1: Extract ---")
    
    # Query as provided in assignment 
    query = """
    query Bets {
      v3Bets(
        first: 1000
        orderBy: createdBlockTimestamp
        orderDirection: desc
        where: {createdBlockTimestamp_gte: "1764460800", createdBlockTimestamp_lt: "1764547200"}
        skip: 0
      ) {
        id
        betId
        bettor
        affiliate
        amount
        odds
        payout
        status
        result
        type
        isCashedOut
        isFreebet
        isRedeemable
        isRedeemed
        createdTxHash
        resolvedTxHash
        redeemedTxHash
        createdBlockTimestamp
        resolvedBlockTimestamp
        redeemedBlockTimestamp
        _subBetsCount
        _wonSubBetsCount
        _lostSubBetsCount
        _canceledSubBetsCount
        selections {
          id
          outcome {
            condition {
              conditionId
              gameId
            }
          }
        }
      }
    }
    """
    
    try:
        response = requests.post(GRAPHQL_URL, json={'query': query})
        response.raise_for_status()
        data = response.json()
        
        if "errors" in data:
            raise Exception(f"GraphQL Error: {data['errors']}")
            
        bets_list = data['data']['v3Bets']
        print(f"Successfully fetched {len(bets_list)} bets.")
        return bets_list
        
    except Exception as e:
        print(f"Extraction Failed: {e}")
        return []


# 2. TRANSFORM
def transform_data(json_data):
    """
    Normalizes JSON, converts timestamps, and strictly enforces SQL schema.
    """
    print("--- Step 2: Transform ---")
    if not json_data:
        print("No data to transform.")
        return None, None

    # --- A. Parent Table (v3_bets) ---
    df_bets = pd.json_normalize(json_data)
    
    # 1. Convert Timestamps (Epoch -> Datetime)
    time_cols = ['createdBlockTimestamp', 'resolvedBlockTimestamp', 'redeemedBlockTimestamp']
    for col in time_cols:
        df_bets[col] = pd.to_datetime(df_bets[col], unit='s', errors='coerce')

    # 2. Rename columns to match SQL Schema
    df_bets = df_bets.rename(columns={
        'id': 'bet_id', 
        'createdBlockTimestamp': 'created_block_timestamp',
        'resolvedBlockTimestamp': 'resolved_block_timestamp',
        'redeemedBlockTimestamp': 'redeemed_block_timestamp',
        'createdTxHash': 'created_tx_hash',
        'resolvedTxHash': 'resolved_tx_hash',
        'redeemedTxHash': 'redeemed_tx_hash',
        'isCashedOut': 'is_cashed_out',
        'isFreebet': 'is_freebet',
        'isRedeemable': 'is_redeemable',
        'isRedeemed': 'is_redeemed',
        '_subBetsCount': 'sub_bets_count',
        '_wonSubBetsCount': 'won_sub_bets_count',
        '_lostSubBetsCount': 'lost_sub_bets_count',
        '_canceledSubBetsCount': 'canceled_sub_bets_count'
    })
    
    # 3. Add Metadata
    df_bets['created_at'] = datetime.utcnow()

    # 4. Strict Column Filtering
    # Only keep columns that actually exist in the DB schema to prevent errors
    target_columns = [
        'bet_id', 'bettor', 'affiliate', 'amount', 'odds', 'payout', 
        'status', 'result', 'type', 'is_cashed_out', 'is_freebet', 
        'is_redeemable', 'is_redeemed', 'created_tx_hash', 
        'resolved_tx_hash', 'redeemed_tx_hash', 'created_block_timestamp', 
        'resolved_block_timestamp', 'redeemed_block_timestamp', 
        'sub_bets_count', 'won_sub_bets_count', 'lost_sub_bets_count', 
        'canceled_sub_bets_count', 'created_at'
    ]
    
    valid_cols = [c for c in target_columns if c in df_bets.columns]
    df_bets_clean = df_bets[valid_cols]

    # --- B. Child Table (v3_bet_selections) ---
    # Explode selections array. Use meta_prefix to distinguish parent ID.
    df_selections = pd.json_normalize(
        json_data, 
        record_path=['selections'], 
        meta=['id'],
        meta_prefix='parent_' 
    )
    
    df_selections = df_selections.rename(columns={
        'parent_id': 'bet_id',
        'id': 'selection_id',
        'outcome.condition.conditionId': 'condition_id', 
        'outcome.condition.gameId': 'game_id'
    })
    
    # Strict filtering for selections
    selection_cols = ['selection_id', 'bet_id', 'condition_id', 'game_id']
    df_selections = df_selections[selection_cols]
    df_selections['created_at'] = datetime.utcnow()
    
    print(f"Transformed: {len(df_bets_clean)} Bets, {len(df_selections)} Selections.")
    return df_bets_clean, df_selections

# 3. LOAD (Upsert Strategy)

def upsert_table(engine, df, table_name, pk_name):
    """
    Performs a PostgreSQL UPSERT (Insert on Conflict Do Update).
    """
    if df.empty:
        return

    # 1. Clean Data: Replace NaT/NaN with Python None (SQL NULL)
    df_clean = df.astype(object).where(pd.notnull(df), None)

    # 2. Reflect Table Schema
    metadata = MetaData()
    try:
        sql_table = Table(table_name, metadata, autoload_with=engine)
    except Exception as e:
        print(f"Error finding table {table_name}: {e}")
        return

    # 3. Prepare Data
    records = df_clean.to_dict(orient='records')

    # 4. Construct Upsert Statement
    insert_stmt = insert(sql_table).values(records)
    
    # Update all columns except Primary Key on conflict
    update_dict = {c.name: c for c in insert_stmt.excluded if c.name != pk_name}

    on_conflict_stmt = insert_stmt.on_conflict_do_update(
        index_elements=[pk_name], 
        set_=update_dict
    )

    # 5. Execute
    with engine.begin() as conn:
        conn.execute(on_conflict_stmt)
        print(f"Upserted {len(df)} rows into {table_name}.")

def load_data(df_bets, df_selections):
    """Orchestrator for loading tables."""
    print("--- Step 3: Load ---")
    
    engine_url = f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
    engine = create_engine(engine_url)

    try:
        # Load Parent Table
        upsert_table(engine, df_bets, 'v3_bets', 'bet_id')
        
        # Load Child Table
        upsert_table(engine, df_selections, 'v3_bet_selections', 'selection_id')
        
        print("ETL Pipeline Completed Successfully.")
            
    except Exception as e:
        print(f"Load Failed: {e}")


# MAIN EXECUTION

if __name__ == "__main__":
    # 1. Extract
    raw_data = extract_data()
    
    # 2. Transform
    bets_df, selections_df = transform_data(raw_data)
    
    # 3. Load
    if bets_df is not None:
        load_data(bets_df, selections_df)