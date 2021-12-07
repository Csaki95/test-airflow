from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'inclouded',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='hello_world',
    description='test dag',
    default_args=default_args
) as dag:
    task1 = BashOperator(
        task_id='hello_world',
        bash_command='echo Hello World!',
        start_date=datetime(2021, 12, 6, 1)
    )

    task1