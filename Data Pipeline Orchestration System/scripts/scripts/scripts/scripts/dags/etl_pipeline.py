from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta


from scripts.extract import extract
from scripts.transform import transform
from scripts.load import load
from scripts.data_quality import check_quality


DEFAULT_ARGS = {
'owner': 'airflow',
'depends_on_past': False,
'email': ['alert@example.com'],
'email_on_failure': True,
'email_on_retry': False,
'retries': 3,
'retry_delay': timedelta(minutes=2),
'sla': timedelta(minutes=10)
}


with DAG(
dag_id='etl_data_pipeline',
default_args=DEFAULT_ARGS,
description='End-to-End ETL Pipeline with SLA & Alerts',
schedule_interval='@daily',
start_date=days_ago(1),
catchup=False,
tags=['etl', 'data-engineering']
) as dag:


extract_task = PythonOperator(
task_id='extract_data',
python_callable=extract
)


transform_task = PythonOperator(
task_id='transform_data',
python_callable=transform
)


load_task = PythonOperator(
task_id='load_data',
python_callable=load
)


quality_task = PythonOperator(
task_id='data_quality_check',
python_callable=check_quality
)


extract_task >> transform_task >> load_task >> quality_task