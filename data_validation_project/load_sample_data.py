import yaml 
import pandas as pd
import sqlite3
from datetime import datetime

# Ingest sample data into SQLite database
def load_config():
    with open('config.yaml', "r") as file:
        data=yaml.safe_load(file)
    return data

def read_data():

    config=load_config()

    df=(
        (pd.read_csv('healthcare_noshows_appt.csv'))
        .rename(columns=config['rename_columns'])
        .astype(dtype=config['dtypes'])
    )
    for column in ['scheduled_day', 'appointment_day']:
        df[column] = pd.to_datetime(df[column])
    
    print(df.head)

    return df

def load_to_database():
    # connect to SQLite database
    conn = sqlite3.connect('data_quality_project.db')
    # cursor to interact with the database
    cursor = conn.cursor()
    # create table if doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS healthcare_appointments (
        patient_id numeric NOT NULL,
        appointment_id numeric NOT NULL,
        gender text,
        scheduled_day date NOT NULL,
        appointment_day date NOT NULL,
        age numeric,
        neighbourhood text,
        scholarship  boolean,
        hypertension boolean,
        diabetes boolean,
        alcoholism boolean,
        handicap boolean,
        sms_received boolean,
        showed_up boolean,
        days_diff numeric
    )
    ''')
    # read and clean dataframe 
    df=read_data()
    # Insert the DataFrame into the 'my_data' table
    df.to_sql('healthcare_appointments', conn, if_exists='replace', index=False)
    # commit the changes 
    conn.commit()

    # Select all rows from the table
    cursor.execute("SELECT * FROM healthcare_appointments")
    # Fetch all rows and print them
    rows = cursor.fetchall()
    if rows:
        if len(rows) == df.shape[0]:
            print("Data loaded successfully")
        else:
            print("Not all data loaded successfully")
    else:
        print("Data not Loaded Successfully")
    # Close the connection
    conn.close()


load_to_database()