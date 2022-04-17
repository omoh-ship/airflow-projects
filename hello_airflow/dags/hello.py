from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta


with DAG(dag_id="sample_program",schedule_interval=timedelta(days=1),start_date=datetime(2021, 1, 1), catchup=False) as dag:
    print_hello = BashOperator(task_id="print_hello", bash_command="echo hello")
    print_world = BashOperator(task_id="print_world", bash_command="echo world")
    
    print_hello >> print_world

