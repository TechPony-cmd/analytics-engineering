import sqlite3

def validating_data_in_SQLite():
    conn = sqlite3.connect('data_quality_project.db')
    cursor = conn.cursor()

    # Query to check for duplicate entries
    cursor.execute("SELECT *, count(*) FROM healthcare_appointments group by patient_id, appointment_id,gender,scheduled_day, appointment_day,age,neighbourhood,scholarship,hypertension,diabetes,alcoholism,handicap,sms_received,showed_up, days_diff having count(*) > 1")
    duplicate_records = cursor.fetchall()

    if duplicate_records:
        print("Duplicate Records found:", duplicate_records)
    else:
        print("No Duplicate Records detected.")

    # Query to check for missing values in columns
    cursor.execute("SELECT * FROM healthcare_appointments WHERE scholarship IS NULL OR hypertension IS NULL OR diabetes IS NULL OR alcoholism IS NULL OR handicap IS NULL OR sms_received IS NULL OR showed_up IS NULL")
    missing_values = cursor.fetchall()

    if missing_values:
        print("Missing values found:", missing_values)
    else:
        print("No missing values detected.")
    
    # Query to check for uniqueness in appointment_id
    cursor.execute("SELECT appointment_id FROM healthcare_appointments group by appointment_id having count(*) > 1")
    duplicate_appointment_id = cursor.fetchall()

    if duplicate_appointment_id:
        print("Duplicate appointment_ids found:", duplicate_appointment_id)
    else:
        print("No duplicate appointment_ids detected.")

    # Query to check for logic errors since appointment date cannot be before scheduled date
    cursor.execute("SELECT * FROM healthcare_appointments where appointment_day < scheduled_day ")
    logic_errors = cursor.fetchall()

    if logic_errors:
        print("Error in appointment day being before scheduled day :", logic_errors)
    else:
        print("Appointment day and scheduled day look accurate.")

    conn.close()

validating_data_in_SQLite()