**Azure Databricks People Analytics Lakehouse
Engineering Handover / Learning Notes**

Project: Enterprise People Analytics Lakehouse on Azure Databricks

Cloud: Microsoft Azure

Platform: Azure Databricks

Architecture: Medallion Lakehouse (Bronze → Silver → Gold)

Final Goal

Build an enterprise-grade HR Analytics platform that demonstrates professional Azure Data Engineering skills.

Instead of simply analysing CSV files, we are building a production-style lakehouse similar to what companies like Rio Tinto, Microsoft, Deloitte or Accenture would implement.

The finished project will include:

Azure Data Lake Storage Gen2
Unity Catalog
Managed Identity Authentication
External Locations
Bronze Layer (Raw)
Silver Layer (Clean)
Gold Layer (Business)
Power BI Dashboard
Delta Lake
Data Quality Checks
Production Notebook Structure
Project Architecture
Azure Storage
       │
       ▼
External Location
       │
       ▼
Bronze Layer
(Raw Delta Tables)
       │
       ▼
Silver Layer
(Clean Business Tables)
       │
       ▼
Gold Layer
(KPI & Analytics)
       │
       ▼
Power BI Dashboard
**Sprint 1 — Azure Environment Setup**
Objective

Create an enterprise Azure environment.

Completed
Azure Subscription created
Azure Resource Group created
Azure Databricks Workspace created
Azure Storage Account created
Bronze Cluster created
Learned

Azure Storage is where enterprise data lives.

Databricks performs computation but does not permanently store business data.

**Sprint 2 — Azure Data Lake Storage (ADLS Gen2)**
Objective

Create enterprise storage.

Completed

Created Storage Account

peopleanalyticslakedomma

Created container

people-data

Uploaded HR datasets

employees.csv
departments.csv
locations.csv
payroll.csv
training.csv
engagement.csv
leave.csv
Learned

ADLS Gen2 is Microsoft's enterprise data lake.

It stores files efficiently and securely.

**Sprint 3 — Unity Catalog**
Objective

Create enterprise governance.

Completed

Created Catalog

rio_dataengineering

Created Schemas

bronze
silver
Learned

Unity Catalog manages

tables
permissions
governance
metadata

Instead of storing random files, enterprise companies organize everything inside catalogs and schemas.

**Sprint 4 — Managed Identity**
Objective

Avoid passwords.

Completed

Configured

Access Connector
Managed Identity
Storage Credential
Biggest Lesson

Never use Storage Keys in enterprise systems.

Enterprise Azure uses

Managed Identity

instead of

Account Keys

No passwords.

No secrets.

Azure authenticates automatically.

Sprint 5 — External Location
Objective

Connect Databricks to Azure Storage securely.

Completed

Created External Location

people_data

using

people_lake_cred
Biggest Lesson

Databricks never reads Azure Storage directly.

Instead

Notebook
↓

External Location

↓

Storage Credential

↓

Managed Identity

↓

Azure Storage
Sprint 6 — Bronze Layer
Objective

Load raw data.

Completed

Created Bronze schema

rio_dataengineering.bronze

Imported

employees

departments

locations

payroll

training

engagement

leave

Saved everything as

Delta Tables

Learned

Bronze contains

Raw

Original

Untouched

Business Data

No transformations.

Sprint 7 — Delta Lake
Objective

Convert CSV into enterprise tables.

Completed

All CSV files converted into

Delta Tables

Examples

bronze.employees

bronze.payroll

bronze.training
Learned

Delta Lake provides

ACID Transactions
Versioning
Faster Reads
Time Travel
Schema Enforcement

Much better than CSV.

Sprint 8 — Multi-table Ingestion
Objective

Automate loading.

Instead of writing

employees

departments

locations

one by one,

built a loop.

Example

for table in tables:
    read csv
    save delta
Learned

Professional engineers automate repetitive work.

Sprint 9 — Bronze Validation
Objective

Verify Bronze Layer.

Validated

Row counts
Table creation
Schemas
Sample data

Confirmed

employees

departments

locations

payroll

training

engagement

leave

all successfully loaded.

Learned

Never trust ingestion until it is validated.

**Sprint 10 — Silver Layer**
Objective

Transform raw data into business-ready datasets.

Completed

Created

silver

schema.

Built

silver.departments

silver.locations

silver.payroll

silver.employees

Started building

employee_profile
Transformations

Examples

Employee IDs

trim()

uppercase()

Names

InitCap()

Emails

lower()

Dates

to_date()

Added

Full Name

Age

Tenure

Active Flag

Quality Flags

Payroll

Added

Gross Pay

Locations

Standardized

Region

Country

City

Departments

Removed duplicates

Trimmed IDs

Normalized names

Remaining Sprint 10

Still to build

silver.training

silver.engagement

silver.leave

employee_profile

Then validate entire Silver Layer.

**Sprint 11 — Gold Layer**

Goal

Business Analytics.

We'll build analytical tables like

gold.employee_metrics

gold.payroll_summary

gold.training_summary

gold.engagement_summary

gold.leave_summary

These will be optimized for reporting.

Planned Sprint 12 — Power BI

Create executive dashboard.

Examples

Headcount

Attrition

Salary Distribution

Department Breakdown

Average Salary

Training Hours

Engagement Score

Leave Utilisation

Average Tenure

Gender Distribution

Country Distribution

Planned Sprint 13 — Production Pipeline

Automate everything.

Instead of clicking Run,

Databricks Jobs will execute

Bronze

↓

Silver

↓

Gold

↓

Power BI Refresh

every day automatically.

Planned Sprint 14 — Data Quality

Enterprise validation.

Examples

Null Checks

Duplicate Checks

Schema Validation

Business Rules

Row Count Validation

Data Freshness

Planned Sprint 15 — Portfolio Completion

Prepare professional GitHub portfolio.

Include

Architecture Diagram
Notebook Documentation
README
Screenshots
Power BI Dashboard
Azure Architecture
Lessons Learned
Business Use Cases
Technologies Used

Cloud

Microsoft Azure

Storage

Azure Data Lake Storage Gen2

Compute

Azure Databricks

Catalog

Unity Catalog

Storage Format

Delta Lake

Language

Python
PySpark
SQL

Visualization

Power BI (planned)
Enterprise Concepts Learned

By the end of this project you will have hands-on experience with:

Azure Resource Groups
Azure Storage
ADLS Gen2
Unity Catalog
Managed Identity
Storage Credentials
External Locations
Delta Lake
Medallion Architecture
Bronze Layer
Silver Layer
Gold Layer
PySpark Data Engineering
Delta Tables
Data Cleansing
Data Quality
Data Modeling
Analytics Engineering
Power BI Integration
Production Pipelines
Engineering Principles We Follow

Throughout this project we've deliberately taken an enterprise approach rather than the quickest approach. That means:

Security first: Managed Identities instead of storage keys.
Governed data access: Unity Catalog, Storage Credentials, and External Locations.
Layered architecture: Bronze (raw), Silver (clean), Gold (business-ready).
Automation over manual work: loops and reusable code instead of repetitive notebook cells.
Validation at every stage: we confirm schemas, row counts, and data quality before moving on.
Production mindset: each notebook represents a stage in a real data pipeline rather than a one-off analysis.



Current Project Status
Sprint	Status
Sprint 1 – Azure Setup	✅ Complete
Sprint 2 – ADLS Gen2	✅ Complete
Sprint 3 – Unity Catalog	✅ Complete
Sprint 4 – Managed Identity	✅ Complete
Sprint 5 – External Location	✅ Complete
Sprint 6 – Bronze Layer	✅ Complete
Sprint 7 – Delta Tables	✅ Complete
Sprint 8 – Automated Ingestion	✅ Complete
Sprint 9 – Bronze Validation	✅ Complete
Sprint 10 – Silver Transformations	🟡 In Progress (~50–60% complete)
Sprint 11 – Gold Layer	⏳ Planned
Sprint 12 – Power BI Dashboard	⏳ Planned
Sprint 13 – Production Pipeline	⏳ Planned
Sprint 14 – Data Quality Framework	⏳ Planned
Sprint 15 – Portfolio & Documentation	⏳ Planned
