# Use the official Astronomer runtime image
FROM quay.io/astronomer/astro-runtime:12.7.1

# Install PySpark
RUN pip install pyspark

# Switch to root user for installing Java
USER root

# Install Java (using default JDK for compatibility)
RUN apt-get update && apt-get install -y default-jdk

# Set Java environment variables
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Increase Airflow webserver timeout
ENV AIRFLOW__WEBSERVER__WEB_SERVER_WORKER_TIMEOUT=300

# Switch back to Astro user for security
USER astro
