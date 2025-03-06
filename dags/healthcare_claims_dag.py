from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Path to your DBT project
dbt_project_path = '/healthcare_claims_project'

# Define your DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'dbt_models_parallel',
    default_args=default_args,
    description='Run healthcare claims dbt models',
    schedule_interval= '0 9 * * *',
    start_date=datetime(2025, 3, 5),
    catchup=False,
)

# List of DBT models to run in parallel
dbt_models = [
    'claims_aging', 
    'claims_payment_status',
    'claims_summary',
    'provider_performance',
    'duplicate_claims',
    'suspicious_diagnosis_procedures',
    'suspicious_providers',
]

# Generating tasks to run each DBT model in parallel
dbt_tasks = []
for model in dbt_models:
    task = BashOperator(
        task_id=f'run_dbt_{model}',
        bash_command=f'cd {dbt_project_path} && dbt run --models {model}', 
        dag=dag,
    )
    dbt_tasks.append(task)