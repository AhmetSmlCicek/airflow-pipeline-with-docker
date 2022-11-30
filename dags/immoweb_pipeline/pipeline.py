from datetime import datetime, timedelta, date
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.docker_operator import DockerOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.dummy_operator import DummyOperator
from docker.types import Mount
import os



default_args = {
    'owner'                 : 'airflow',
    'description'           : 'Data pipeline for immo eliza',
    'depend_on_past'        : False,
    'start_date'            : datetime(2022, 11, 21),
    'email_on_failure'      : False,
    'email_on_retry'        : False,
    #'retries'               : 1,
    #'retry_delay'           : timedelta(minutes=5)
}

with DAG('immo-eliza-pipeline', default_args=default_args, schedule_interval="@daily", catchup=False) as dag:
    dag_start = DummyOperator(
        task_id='dag_start'
        )    
        
    t1 = DockerOperator(
        task_id='scraping',
        image='airflow_scraper:latest',
        container_name='task___scraper',
        api_version='auto',
        auto_remove=True,
        #command=,
        #mounts=[Mount(source="/home/becode2/Desktop/becode_2022/airflow-with-docker/dags/immoweb_pipeline/data",
                      #target='/custom_data',
                      #type='volume')]
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        mount_tmp_dir=False,
        environment={
            "AZURE_CONNECTION_STRING": os.getenv("AZURE_CONNECTION_STRING"),
            "STORAGE_CONTAINER": os.getenv("STORAGE_CONTAINER")
        }
        )

    t2 = DockerOperator(
        task_id='cleaning',
        image='airflow_cleaner:latest',
        container_name='task___cleaning',
        api_version='auto',
        auto_remove=True,
        #command="python3 model/model.py",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        environment={
            "AZURE_CONNECTION_STRING": os.getenv("AZURE_CONNECTION_STRING"),
            "STORAGE_CONTAINER": os.getenv("STORAGE_CONTAINER")
        }
        )

    t3 = DockerOperator(
        task_id='preprocess',
        image='airflow_preprocessing:latest',
        container_name='task___preprocess',
        api_version='auto',
        auto_remove=True,
        #command="python3 sql/sql.py",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        environment={
            "AZURE_CONNECTION_STRING": os.getenv("AZURE_CONNECTION_STRING"),
            "STORAGE_CONTAINER": os.getenv("STORAGE_CONTAINER")
        }
        )
    
    t4 = DockerOperator(
        task_id='model',
        image='airflow_training:latest',
        container_name='task___training',
        api_version='auto',
        auto_remove=True,
        #command="python3 visualization/visualization.py",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        environment={
            "AZURE_CONNECTION_STRING": os.getenv("AZURE_CONNECTION_STRING"),
            "STORAGE_CONTAINER": os.getenv("STORAGE_CONTAINER")
        }
        
        )


    dag_end = BashOperator(
        task_id='dag_end',
        bash_command=f"echo 'end run timestamp: {datetime.now()}' >> /opt/airflow/data/run_log.txt"
        )    

    dag_start >> t1 
    
    t1 >> t2 >> t3 >> t4

    t4 >> dag_end