from pyspark.sql import SparkSession
from airflow.models import Variable

# Function to run a PySpark job
def run_spark_job():
    # Initialize Spark session
    spark = SparkSession.builder \
        .appName("Airflow PySpark Job") \
        .master("local[*]") \
        .getOrCreate()
    
    # Retrieve the file path from Airflow Variable
    path = Variable.get("path_to_spark", "customers.csv")
    print("Variable retrieved successfully")
    
    # Read CSV file into a DataFrame
    df = spark.read.csv(path, header=True, inferSchema=True)
    
    # Display the DataFrame contents
    df.show()
    
    # Stop Spark session
    spark.stop()
