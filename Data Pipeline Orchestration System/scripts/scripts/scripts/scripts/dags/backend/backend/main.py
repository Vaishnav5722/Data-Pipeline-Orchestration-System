from fastapi import FastAPI
import requests


AIRFLOW_API = "http://airflow-webserver:8080/api/v1"
USERNAME = "airflow"
PASSWORD = "airflow"


app = FastAPI(title="Pipeline Monitoring API")


@app.get("/health")
def health():
return {"status": "Backend running"}


@app.get("/dags")
def list_dags():
r = requests.get(f"{AIRFLOW_API}/dags", auth=(USERNAME, PASSWORD))
return r.json()


@app.get("/dags/{dag_id}/runs")
def dag_runs(dag_id: str):
r = requests.get(
f"{AIRFLOW_API}/dags/{dag_id}/dagRuns",
auth=(USERNAME, PASSWORD)
)
return r.json()