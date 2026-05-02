-- 1. Create the PARENT table (The Bet)
CREATE TABLE IF NOT EXISTS v3_bets (
    bet_id VARCHAR(255) PRIMARY KEY,        -- The unique ID for the bet 
    bettor VARCHAR(255),                    -- Who made the bet
    affiliate VARCHAR(255),                 -- Affiliate ID
    amount NUMERIC,                         -- Value of the bet
    odds NUMERIC,                           -- Odds at the time of placing
    payout NUMERIC,                         -- Winnings (if any)
    status VARCHAR(50),                     -- Status (Resolved, Canceled, etc.)
    result VARCHAR(50),                     -- Result (Won, Lost)
    type VARCHAR(50),                       -- Ordinar vs Express [cite: 41]
    is_cashed_out BOOLEAN,
    is_freebet BOOLEAN,
    is_redeemable BOOLEAN,
    is_redeemed BOOLEAN,
    created_tx_hash VARCHAR(255),           -- Blockchain transaction hash
    resolved_tx_hash VARCHAR(255),
    redeemed_tx_hash VARCHAR(255),
    created_block_timestamp TIMESTAMP,      -- Converted UTC timestamp [cite: 46]
    resolved_block_timestamp TIMESTAMP,
    redeemed_block_timestamp TIMESTAMP,
    sub_bets_count INT,                     -- Count fields from the API
    won_sub_bets_count INT,
    lost_sub_bets_count INT,
    canceled_sub_bets_count INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Required Metadata 
);


CREATE TABLE IF NOT EXISTS v3_bet_selections (
    selection_id VARCHAR(255) PRIMARY KEY,
    bet_id VARCHAR(255),
    condition_id VARCHAR(255),
    game_id VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_bet FOREIGN KEY (bet_id) REFERENCES v3_bets (bet_id) ON DELETE CASCADE
);