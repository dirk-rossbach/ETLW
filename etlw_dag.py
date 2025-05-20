from __future__ import annotations

import pendulum

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="etlw_process",
    schedule=None,
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
    tags=["etlw"],
) as dag:
    bash_task = BashOperator(
        task_id="placeholder_task",
        bash_command="echo 'ETLW DAG is running!'",
    )