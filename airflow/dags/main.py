from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import os



default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=5),
}

# Paths
scripts_dir = "../scripts"
data_path = "../data/Amazon Sale Report.csv"
sql_script_path = "../sql_files/roleup_materialized.sql"

dag = DAG(
    'visualization_pipeline',
    default_args = default_args,
    description='Load, transform, and visualize data pipeline',
    schedule_interval=None,
    start_date=datetime(2024, 12, 28),
)




