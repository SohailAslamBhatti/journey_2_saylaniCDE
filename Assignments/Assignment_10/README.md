

---

### **Objective**

The objective of this project is to build an end-to-end data pipeline using Airflow on AWS EC2 to load data from S3 into Snowflake with automated email notifications.

**Key Learning Outcomes:**

* Understanding Apache Airflow architecture (Scheduler, Webserver, Worker)
* Creating and managing DAGs in Airflow
* Monitoring files in Amazon S3 using S3 Sensor
* Automating data loading into Snowflake
* Using SnowflakeOperator for data ingestion
* Sending email notifications using SMTP
* Managing secrets using AWS Secrets Manager
* Logging and monitoring using CloudWatch

---

### **Prerequisites**

* AWS account with EC2 instance configured
* Basic knowledge of Apache Airflow
* Snowflake account with required roles and warehouse
* S3 bucket with sample data file
* SMTP/email configuration for notifications

---

### **Tech Stack**

* **Language:** Python, SQL
* **Tools/Services:** Apache Airflow, AWS EC2, Amazon S3, Snowflake, AWS Secrets Manager, CloudWatch

---

### **Project Workflow**

1. **S3 Sensor** detects new file in S3 bucket
2. **Airflow DAG** is triggered
3. **Table Creation Task** creates table in Snowflake (if not exists)
4. **Data Load Task** copies data from S3 to Snowflake
5. **Notification Task** sends email after successful execution

---

### **Project Structure**

```
airflow-s3-snowflake-pipeline/
├── dags/
│   └── pipeline_dag.py            # Main Airflow DAG
├── scripts/
│   └── snowflake_queries.sql     # SQL queries for table and load
├── config/
│   └── airflow_connections.json  # Connection configs (optional)
├── data/
│   └── sample_file.csv           # Sample data in S3
├── img/
│   └── architecture.png          # Architecture diagram
└── README.md
```

---

### **File Descriptions**

* **pipeline_dag.py** – Defines Airflow DAG with all tasks (Sensor, Load, Notification)
* **snowflake_queries.sql** – SQL commands for table creation and data loading
* **airflow_connections.json** – Stores Airflow connection configurations
* **data/** – Sample dataset used for testing
* **img/** – Architecture diagram of pipeline

---

If you want, I can also:

* Add **step-by-step setup (EC2 + Airflow installation)**
* Provide **complete DAG code**
* Convert this into a **strong portfolio project for LinkedIn/GitHub** 👍
