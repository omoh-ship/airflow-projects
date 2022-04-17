from airflow.models import DagBag
from airflow.operators.python import PythonOperator, BranchPythonOperator
import pytest
import mocking 
from datetime import datetime 
import pendulum
from airflow.utils.trigger_rule import TriggerRule


@pytest.fixture
def dagbag():
    return DagBag(include_examples=False)

	
def test_dagbag(dagbag):
	"""Test to see if dag was loaded properly and includes sanity checks e.g if dag has unque dag_id"""
	dag = dagbag.get_dag(dag_id="mocking_dag")
	assert dagbag.import_errors == {}
	assert dag is not None
	

def test_task_training_model_a(dagbag, mocker):
	"""Tests that a task returns a value"""
	_training_model_a = mocker.patch('mocking._training_model_a', return_value=9) 
	expected_start = datetime(2021, 1, 1)
	dag = dagbag.get_dag(dag_id="mocking_dag")
	test = PythonOperator(dag=dag, task_id="test", python_callable=_training_model_a)
	result = test.execute(context={})
	assert result == 9
	

def test_tasks_in_correct_order(dagbag):
	"""Tests if tasks will be executed in correct order."""
	dag = dagbag.get_dag(dag_id="mocking_dag")
	training_model_a = dag.get_task("training_model_a")
	training_model_b = dag.get_task("training_model_b")
	training_model_c = dag.get_task("training_model_c")
	choose_best_model = dag.get_task("choose_the_best_model")
	accurate = dag.get_task("accurate")
	inaccurate = dag.get_task("inaccurate")
	
	assert training_model_a.downstream_list == [choose_best_model]
	assert training_model_b.downstream_list == [choose_best_model]
	assert training_model_c.downstream_list == [choose_best_model]
	
	assert choose_best_model.downstream_list == [accurate, inaccurate]

	