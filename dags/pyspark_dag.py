from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime
from dags.scripts.myspark import run_spark_job  # Importing PySpark job function

# Function to set an Airflow Variable for the Spark job
def set_path_variable():
    Variable.set("path_to_spark", "customers.csv")  # Setting the variable value
    print("Variable set successfully")

# Default arguments for the DAG
default_args = {
    "owner": "airflow",
    "start_date": datetime(2025, 3, 14),  # DAG start date
    "retries": 1,  # Number of retry attempts
}

# Defining the DAG
with DAG(
    dag_id="pyspark_dag",
    default_args=default_args,
    schedule_interval=None,  # Manual trigger only
    catchup=False,  # Prevents backfilling
) as dag:
    
    # Task to set Airflow Variable
    set_path = PythonOperator(
        task_id="set_path",
        python_callable=set_path_variable
    )
    
    # Task to execute the PySpark job
    spark_task = PythonOperator(
        task_id="run_spark_job",
        python_callable=run_spark_job  # Calls the PySpark function
    )

    # Task dependency
    set_path >> spark_task  # Ensures `set_path` runs before `spark_task`
