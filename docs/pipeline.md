# Pipeline

## Step 1

Read CSV files from Azure Data Lake.

## Step 2

Write Delta tables into Bronze.

Tables

- employees
- departments
- locations
- payroll
- training
- engagement
- leave

## Step 3

Transform Bronze into Silver.

Tasks

- remove duplicates
- validate dates
- calculate leave days
- enrich employee profiles
- standardise schemas

## Step 4

Create Gold reporting tables.

Examples

- Headcount by department
- Payroll summary
- Training summary
- Engagement summary

## Step 5

Run automated data-quality checks.

## Step 6

Write pipeline audit log.
