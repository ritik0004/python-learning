# DGbet ETL Pipeline Assignment

## Overview
This project implements a robust ETL (Extract, Transform, Load) pipeline that fetches betting data from the Azuro Protocol via The Graph API, normalizes the nested JSON structure, and loads it into a PostgreSQL database.

The solution is designed to be **idempotent** and **fault-tolerant**, capable of running on a daily schedule without creating duplicate records or data integrity issues.

## Architecture Decisions

### 1. Containerized Database (Docker)
To satisfy the requirement for a "Postgres SQL DB within a VM environment," this project uses **Docker**.

### 2. Idempotency Strategy (Upsert)
The assignment requires the routine to be run daily.
- **Approach:** Instead of a naive `INSERT` (which fails on duplicates) or a `DELETE` + `INSERT` (which risks data loss if the script crashes mid-process), I implemented a **PostgreSQL UPSERT** (`INSERT ... ON CONFLICT DO UPDATE`).
- **Benefit:** This ensures atomicity. Existing records are updated with the latest status (e.g., `Pending` -> `Resolved`), and new records are inserted seamlessly.

### 3. Data Normalization
The raw JSON contains nested `selections` arrays.
- **Schema:** I normalized this into a Parent-Child relationship:
  - `v3_bets` (Parent): Contains metadata, odds, and status.
  - `v3_bet_selections` (Child): Contains specific outcomes, linked via Foreign Key (`bet_id`).
- **Strict Typing:** Timestamps are converted from Epoch (Unix) to proper SQL `TIMESTAMP` format for easier querying.

---

## Setup & Execution

### Prerequisites
- Docker Desktop
- Python 3.9+

### Step 1: Start the Database
Spin up the isolated Postgres container:
```bash
docker run --name dgbet-postgres -e POSTGRES_PASSWORD=mysecretpassword -e POSTGRES_DB=dgbet_db -p 5432:5432 -d postgres

```

### Step 2: Install Python Dependencies

```bash
pip install pandas sqlalchemy psycopg2-binary requests

```

### Step 3: Initialize Schema (Optional)

The Python script is capable of auto-generating the table structure using SQLAlchemy reflection. However, a raw SQL schema file (`schema.sql`) is provided for reference and manual creation if preferred.

### Step 4: Run the Pipeline

Execute the ETL script:

```bash
python etl.py

```

## 📂 Project Structure

* **`etl_assignment.py`**: Main application code containing Extract, Transform, and Load logic.
* **`schema.sql`**: DDL commands for table creation.
* **`README.md`**: Project documentation.
* **`/screenshots`**: Evidence of DB Schema and Data Validation.
