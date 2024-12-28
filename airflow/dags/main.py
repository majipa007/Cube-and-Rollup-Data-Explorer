from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import os
from scripts import data_transformer, data_loader


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=5),
}

# Paths
data_path = "/opt/airflow/data/Amazon Sale Report.csv"
sql_script_path = "/opt/airflow/sql_files/roleup_materialized.sql"
viz_path = "/opt/airflow/scripts/viz.py"

def load_data():
    data_loader(data_path)

def transform_data():
    data_transformer(sql_script_path)

with DAG(
    'visualization_pipeline',
    default_args = default_args,
    description='Load, transform, and visualize data pipeline',
    schedule_interval=None,
    start_date=datetime(2024, 12, 28),
) as dag:
    start = DummyOperator(task_id='start_task')

    load = PythonOperator(
        task_id='load_data',
        python_callable=load_data
    )

    transform = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data
    )

    viz = BashOperator(
        task_id='run_viz',
        execution_timeout=timedelta(minutes=1),  # Stop task if it runs for more than 1 hour
        bash_command=f"streamlit run {viz_path}"# --server.port=8501 --server.address=0.0.0.0 --server.headless=true"
    )

    start >> load >> transform >> viz




