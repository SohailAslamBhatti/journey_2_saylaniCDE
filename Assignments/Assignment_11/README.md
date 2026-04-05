
![img-snowflake-loading](./img/assignment10a.jpg)

### **Objective**

The objective of this project is to gain hands-on experience with Snowflake and AWS through practical learning.

**Key Learning Outcomes:**

* Overview of Snowflake
* Loading data using Web UI and SnowSQL (CLI)
* Loading data from Amazon S3 (via keys and storage integration)
* Real-time data loading using Snowpipe
* Data visualization using AWS QuickSight
* Understanding Snowflake pricing
* Time Travel feature in Snowflake
* Performance optimization techniques

---

### **Prerequisites**

* Snowflake account with active warehouse and required roles
* SnowSQL (CLI) installed (optional)
* AWS account with S3 bucket and credentials/IAM role (for S3 loading)

---

### **Tech Stack**

* **Language:** SQL
* **Tools/Services:** Snowflake, SnowSQL, Amazon S3, AWS QuickSight

---

### **Project Structure**

```
snowflake-loading-data/
├── README.md
├── snowflake-loading.sql
├── s3_policy.txt
├── trust_policy.txt
├── dataset/
│   ├── customer_detail.csv
│   ├── TSLA.csv
│   └── TSLA_modified.csv
└── image/
    └── assignment10a.jpg
```

---

### **File Descriptions**

* **snowflake-loading.sql** – SQL scripts for tables, stages, COPY, Snowpipe, and Time Travel
* **dataset/** – Sample CSV files for practice
* **image/** – Diagrams of data loading flow
* **s3_policy.txt** – S3 bucket access policy
* **trust_policy.txt** – IAM trust policy for Snowflake

