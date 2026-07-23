"""
LevelUp Airflow Masterclass — Hands-On Lab
Demo 1: HELLO AIRFLOW
"""
 
import pendulum
 
from airflow.decorators import dag, task
 
 
@dag(
    dag_id="01_hello_airflow",
    schedule=None,
    start_date=pendulum.datetime(2026, 1, 1, tz="Asia/Kolkata"),
    catchup=False,
    tags=["levelup", "lab", "1-beginner"],
    doc_md=__doc__,
)
def hello_airflow():
 
    @task()
    def say_hello():
        print("=" * 50)
        print("Hello from Airflow! Your very first task just ran.")
        print("Deployed automatically via GitHub Actions.")
        print("=" * 50)
        return "hello done"
 
    say_hello()
 
 
hello_airflow()
