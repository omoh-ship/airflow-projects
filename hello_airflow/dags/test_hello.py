from airflow.models import DagBag
import pytest
import pendulum


@pytest.fixture
def dagbag():
    return DagBag(include_examples=False)


def test_dagbag(dagbag):
	"""Test to see if dag was loaded properly and includes sanity checks e.g if dag has unque dag_id"""
	dag = dagbag.get_dag(dag_id="sample_program")
	assert dagbag.import_errors == {}
	assert dag is not None


def test_etl_dag_has_catchup_set_to_true(dagbag):
	"""Test to see if catchup is set to false"""
	dag = dagbag.get_dag(dag_id="sample_program")
	assert not dag.catchup
	
	
def test_etl_dag_starts_on_correct_date(dagbag):
	"""Test to see if dag starts on correct date"""
	dag = dagbag.get_dag(dag_id="sample_program")
	assert dag.start_date == pendulum.datetime(2021, 1, 1)

	

def test_tasks_in_correct_order(dagbag):
	"""Tests if tasks will be executed in correct order."""
	dag = dagbag.get_dag(dag_id="sample_program")
	
	print_hello = dag.get_task("print_hello")
	print_world = dag.get_task("print_world")
	
	assert print_world.upstream_list == [print_hello]
	