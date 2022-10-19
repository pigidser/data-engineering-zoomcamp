# This folder contains my attempt to set up Airflow environment with Docker.

Download template:

```bash
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'
```

Update as described.

Build docker, initialize airflow and up docker compose:
```bash
docker compose build
docker compose up airflow-init
docker compose up -d
```