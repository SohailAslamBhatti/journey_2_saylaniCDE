![Project-17](./images/asgnmt17.png)

**WORKFLOW** Here is the step-by-step workflow for the **Serverless DataLake Architecture** on AWS:

---

### Step 1: Data Ingestion

* **S3 Bucket (CSV):** The process begins when a CSV data file is uploaded or ingested into the initial Amazon S3 bucket.

### Step 2: Ingestion Trigger

* **Lambda:** The file upload triggers an AWS Lambda function, which acts as the initial orchestrator to kick off the data processing pipeline.

### Step 3: Schema Discovery & Cataloging

* **AWS Glue Crawler & AWS Glue Catalog:** The Lambda function invokes an AWS Glue Crawler. This crawler scans the CSV data in the S3 bucket to automatically infer its schema and updates the metadata in the AWS Glue Catalog.

### Step 4: Monitoring Crawler Success

* **CloudWatch Rule:** An Amazon CloudWatch Rule monitors the status of the AWS Glue Crawler. Once the crawler successfully finishes cataloging the data, this rule captures the event.

### Step 5: Processing Trigger

* **Lambda:** Upon detecting the crawler's successful completion, the CloudWatch Rule triggers a second AWS Lambda function to initiate the data transformation phase.

### Step 6: ETL / Data Transformation

* **Glue Job:** The second Lambda function kicks off an AWS Glue Job (ETL process). This job processes the raw CSV data, transforms it, and outputs it into an optimized columnar format.
* **S3 Bucket (Parquet) / Processed Data Sink:** The transformed data is saved into a separate target S3 bucket as Parquet files, serving as the final processed data sink.

### Step 7: Final Monitoring & Notification

* **CloudWatch (Monitors Job Success):** A final CloudWatch process monitors the execution status of the AWS Glue Job.
* **SNS Topic:** Once the Glue Job completes successfully, it sends a message or alert via an Amazon SNS (Simple Notification Service) Topic.
* **Gmail / Email Notification:** The SNS topic routes the message to send an automated email notification (visualized by Gmail) to inform stakeholders or administrators that the pipeline run was successful.
