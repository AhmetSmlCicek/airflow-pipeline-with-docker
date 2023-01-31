# About

The goal here is to create ETL pipeline for real-estate property data in Belgium. The pipeline starts with extracting the data from real-estate websites,
continue with cleaning and preprocessing to make data ready for ML model. ML model takes the data and provides price prediction. The pipeline is managed with Apache Airflow and each task is designed as a separate Docker container. 

# How to Run

Start script consists in docker commands to build images and compose up Airflow and other Docker containers. All you need to do is to run this bash script (please pay attention .env command in the script).
