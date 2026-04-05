from airflow import DAG
from datetime import timedelta, datetime
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
from airflow.contrib.operators.snowflake_operator import SnowflakeOperator
from airflow.operators.email import EmailOperator

from scripts.queries import CREATE_TABLE_SQL, COPY_SQL

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 8),
    'email': ['myemail@domain.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=2)
}

s3_prefix = 's3://airflow-snow-email-bucket/city_folder/us_city.csv'
s3_bucket = None

with DAG(
    'snowflake_s3_with_email_notification_etl',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    is_file_in_s3_available = S3KeySensor(
        task_id='tsk_is_file_in_s3_available',
        bucket_key=s3_prefix,
        bucket_name=s3_bucket,
        aws_conn_id='aws_s3_conn',
        poke_interval=3
    )

    create_table = SnowflakeOperator(
        task_id="create_snowflake_table",
        snowflake_conn_id='conn_id_snowflake',
        sql=CREATE_TABLE_SQL
    )

    copy_csv_into_snowflake_table = SnowflakeOperator(
        task_id="tsk_copy_csv_into_snowflake_table",
        snowflake_conn_id='conn_id_snowflake',
        sql=COPY_SQL
    )

    notification_by_email = EmailOperator(
        task_id="tsk_notification_by_email",
        to="tuplespectra@gmail.com",
        subject="Snowflake ETL Pipeline",
        html_content="Data loaded successfully into Snowflake."
    )

    is_file_in_s3_available >> create_table >> copy_csv_into_snowflake_table >> notification_by_email
