# airflow-projects

A collection of airflow projects where DAG the dag scripts schedule tasks.


## Getting Started

### Cloning repo

To clone the repo:

```bash
git clone https://github.com/omoh-ship/airflow-projects.git
```


### Setting up airflow

```bash
export AIRFLOW_HOME=~/airflow-projects/<path to directory to be worked with>

pip install 'apache-airflow==2.2.4' --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.2.4/constraints-3.7.txt"
```

> It is adviced to pip install with constraints because hen pip installs without the constraints, it tends to install packages that might
not be compatible with airflow.

```bash
cd airflow-projects/<path to directory to be worked with>

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
cd airflow-projects/<path to directory to be worked with>/tests

python3 -m pytest -v <test_script>.py
```
