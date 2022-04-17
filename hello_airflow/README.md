# hello_airflow 

A simple DAG that says hello and a unit test to check if components work as expected.


## Getting Started

> Have you recently started using Git? This should give you the base commands you need to perform the most common actions in Git. If you find a command that is not here, or could be explained better, please don't hesitate in * [Contributing](#contributing). Cheers!

### Cloning repo

To clone the repo:

```bash
git clone https://github.com/omoh-ship/airflow-projects.git
```


### Setting up airflow

```bash
export AIRFLOW_HOME=~/airflow-projects/hello_airflow

pip install 'apache-airflow==2.2.4' --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.2.4/constraints-3.7.txt"
```

> It is adviced to pip install with constraints because hen pip installs without the constraints, it tends to install packages that might
not be compatible with airflow.

```bash
cd airflow-projects/hello_airflow

airflow db init

airflow users create \
    --username YourUsername \
    --firstname YourName \
    --lastname YourLastName \
    --role Admin \
    --email youremal@email.org

airflow webserver --port 8080

airflow scheduler
```


## Running the Test Script

```bash
cd airflow-projects/hello_airflow/dags

python3 -m pytest -v test_hello.py
```
