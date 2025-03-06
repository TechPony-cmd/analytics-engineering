# Data Quality Monitoring System

This project automates data quality checks on a sample dataset from Kaggle using sql and Python.

## Steps:
1. **Setup**: Read sample data and initalize local database - SQLite.
2. **Python Unit Testing & SQL Database Checks**: Validate data for missing values, duplicates and any logic errors pre-ingestion (python unit testing) and post-ingestion into database(sql table checks). Post-ingestion Validations are based on the assumption that you only have access to the database table and not the ETL process.

## How to Run:
1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Pre-ingestion Validations.
    ```bash
    python -m unittest unittest_data_quality.py
    ```
3. Set up the database SQLite and load sample data in database.
    ```bash
    python load_sample_data.py
    ```
4. Post-ingestion Validations (Can only access data through the database)
    ```bash
    python sqltest_data_quality.py
    ```