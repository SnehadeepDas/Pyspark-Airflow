# PySpark Connection in Docker with Airflow 🚀🐍🐳💨

### Overview 📖🔍

This project sets up a PySpark environment inside a Docker container and integrates it with Apache Airflow. It allows running PySpark jobs using Airflow, leveraging Airflow Variables to dynamically pass file paths.

### Project Structure 📂🛠

/pyspark-airflow-docker
│── dags/ # Airflow DAGs directory
│ ├── pyspark_dag.py # DAG for running PySpark job
│── scripts/ # Custom Python scripts
│ ├── myspark.py # PySpark job script
│── Dockerfile # Docker setup with PySpark and Java
│── requirements.txt # Python dependencies
│── README.md # Project documentation

### Why Astro + Docker Instead of Local Setup?

✅ Isolation: Running PySpark inside a container ensures no dependency conflicts.
✅ Portability: The setup works on any machine with Docker, without additional configuration.
✅ Ease of Deployment: Astro simplifies managing Airflow without manual installation.
✅ Scalability: If needed, the same setup can run in production environments.

### Setup Instructions ⚙️📝

docker build -t pyspark-airflow .
docker run -p 8080:8080 pyspark-airflow

### Access the Airflow UI 🌐💨

Open http://localhost:8080 in your browser.
Trigger the pyspark_dag to run the PySpark job.

### Challenges Faced & Solutions⚠️✅

### 1. Java Installation for PySpark 🗸

**Issue:** PySpark requires Java, but the container lacked it.
**Solution:** Installed default-jdk in the Dockerfile and set JAVA_HOME.

#### 2. Airflow Variables Not Persisting 🗸

**Issue:** The Airflow Variable storing the file path was not accessible inside PySpark.
**Solution:** Used Variable.get() correctly inside the PySpark script and ensured Airflow was restarted after setting the variable.

#### 3. PySpark Job Execution in Airflow 🗸

**Issue:** The PySpark job was not executing properly when triggered from Airflow.
**Solution:** Installed apache-airflow-providers-apache-spark and properly structured the DAG.

#### Future Enhancements🚀✨

❄️ **_Add support for Snowflake integration._** ❄️
