
# Build images for each tasks
docker build -f dags/immoweb_pipeline/scraping/Dockerfile -t airflow_scraper:latest ./dags/immoweb_pipeline;
docker build -f dags/immoweb_pipeline/cleaning_for_analysis/Dockerfile -t airflow_cleaner:latest ./dags/immoweb_pipeline;
docker build -f dags/immoweb_pipeline/cleaning_for_model/Dockerfile -t airflow_preprocessing:latest ./dags/immoweb_pipeline;
docker build -f dags/immoweb_pipeline/model/Dockerfile -t airflow_training:latest ./dags/immoweb_pipeline;

# Initiate docker airflow
docker compose up airflow-init;

# Start containers from images
docker compose --env-file .env up;

