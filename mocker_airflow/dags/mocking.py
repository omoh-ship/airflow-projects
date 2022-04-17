from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from functions import _training_model_a, _training_model_b, _training_model_c, _choose_best_model


with DAG(dag_id="mocking_dag",schedule_interval=timedelta(days=1),start_date=datetime(2021, 1, 1), catchup=False) as dag:
    # the accuracies of the model is stored in airflow's db
    training_model_a = PythonOperator(task_id="training_model_a", python_callable=_training_model_a)
    training_model_b = PythonOperator(task_id="training_model_b", python_callable=_training_model_b)
    training_model_c = PythonOperator(task_id="training_model_c", python_callable=_training_model_c)
    
    choose_best_model = BranchPythonOperator(task_id="choose_the_best_model", python_callable=_choose_best_model)

    accurate = BashOperator(task_id="accurate", bash_command="echo 'accurate'")
    inaccurate = BashOperator(task_id="inaccurate", bash_command="echo 'inaccurate'")

    [training_model_a, training_model_b, training_model_c] >> choose_best_model >> [accurate, inaccurate]