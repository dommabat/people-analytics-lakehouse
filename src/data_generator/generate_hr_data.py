import pandas as pd
import numpy as np
from faker import Faker
from pathlib import Path
from datetime import datetime, date

fake = Faker()
np.random.seed(42)

OUTPUT_DIR = Path("data/sample")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

NUM_EMPLOYEES = 100

departments = pd.DataFrame({
    "department_id": ["D001", "D002", "D003", "D004", "D005", "D006", "D007"],
    "department_name": ["Operations", "HR", "Finance", "Technology", "Procurement", "HSE", "Legal"]
})

locations = pd.DataFrame({
    "location_id": ["L001", "L002", "L003", "L004", "L005", "L006", "L007", "L008"],
    "city": ["Perth", "Brisbane", "Ulaanbaatar", "Singapore", "Montreal", "London", "Johannesburg", "Salt Lake City"],
    "country": ["Australia", "Australia", "Mongolia", "Singapore", "Canada", "United Kingdom", "South Africa", "United States"],
    "region": ["APAC", "APAC", "APAC", "APAC", "Americas", "EMEA", "EMEA", "Americas"]
})

business_units = ["Iron Ore", "Copper", "Aluminium", "Lithium", "Exploration", "Corporate"]
employment_types = ["Permanent", "Contractor", "Graduate"]
salary_bands = ["A", "B", "C", "D", "E", "F"]

employees = []

for i in range(1, NUM_EMPLOYEES + 1):
    gender = np.random.choice(["Female", "Male", "Other"], p=[0.42, 0.56, 0.02])
    first_name = fake.first_name_female() if gender == "Female" else fake.first_name_male()
    last_name = fake.last_name()

    hire_date = fake.date_between(start_date="-10y", end_date="today")
    terminated = np.random.choice([True, False], p=[0.12, 0.88])

    termination_date = None
    status = "Active"

    if terminated and hire_date < datetime.today().date():
        termination_date = fake.date_between(start_date=hire_date, end_date="today")
        status = "Terminated"

    employees.append({
        "employee_id": f"E{i:06d}",
        "first_name": first_name,
        "last_name": last_name,
        "gender": gender,
        "birth_date": fake.date_between(start_date="-65y", end_date="-21y"),
        "hire_date": hire_date,
        "termination_date": termination_date,
        "employment_status": status,
        "employment_type": np.random.choice(employment_types, p=[0.75, 0.20, 0.05]),
        "department_id": np.random.choice(departments["department_id"]),
        "location_id": np.random.choice(locations["location_id"]),
        "business_unit": np.random.choice(business_units),
        "salary_band": np.random.choice(salary_bands),
        "email": f"{first_name.lower()}.{last_name.lower()}@globalminingcorp.com"
    })

employees = pd.DataFrame(employees)

# Managers: first 500 employees become possible managers
manager_pool = employees["employee_id"].head(500).tolist()
employees["manager_id"] = np.random.choice(manager_pool, size=len(employees))
employees.loc[employees["employee_id"] == employees["manager_id"], "manager_id"] = None

# Payroll: 12 months
payroll_records = []
months = pd.date_range("2025-01-01", "2025-12-01", freq="MS")

salary_map = {
    "A": 3000,
    "B": 4500,
    "C": 6500,
    "D": 9000,
    "E": 12000,
    "F": 16000
}

for _, row in employees.iterrows():
    for month in months:
        if row["termination_date"] and month.date() > row["termination_date"]:
            continue

        base = salary_map[row["salary_band"]]
        overtime = np.random.randint(0, 800)
        bonus = np.random.choice([0, 500, 1000, 2000], p=[0.75, 0.15, 0.07, 0.03])
        tax = round((base + overtime + bonus) * 0.18, 2)

        payroll_records.append({
            "employee_id": row["employee_id"],
            "payroll_month": month.date(),
            "base_salary": base,
            "overtime": overtime,
            "bonus": bonus,
            "tax": tax,
            "net_pay": round(base + overtime + bonus - tax, 2)
        })

payroll = pd.DataFrame(payroll_records)

# Training
training_records = []
courses = ["Safety Induction", "Leadership Basics", "Data Privacy", "Mine Site Safety", "Diversity & Inclusion"]

for _, row in employees.sample(300, replace=True).iterrows():
    training_records.append({
        "employee_id": row["employee_id"],
        "course_name": np.random.choice(courses),
        "completion_date": fake.date_between(start_date=row["hire_date"], end_date="today"),
        "hours": np.random.choice([1, 2, 4, 8, 16]),
        "score": np.random.randint(60, 101),
        "mandatory": np.random.choice([True, False], p=[0.65, 0.35])
    })

training = pd.DataFrame(training_records)

# Engagement
engagement = employees.sample(70).copy()
engagement = engagement[["employee_id"]]
engagement["survey_date"] = "2025-09-30"
engagement["engagement_score"] = np.random.randint(1, 11, size=len(engagement))
engagement["wellbeing_score"] = np.random.randint(1, 11, size=len(engagement))
engagement["manager_score"] = np.random.randint(1, 11, size=len(engagement))

# Leave
leave_records = []
leave_types = ["Annual Leave", "Sick Leave", "Parental Leave", "Unpaid Leave"]

for _, row in employees.sample(200, replace=True).iterrows():
    days = np.random.randint(1, 15)
    leave_records.append({
        "employee_id": row["employee_id"],
        "leave_type": np.random.choice(leave_types),
        "start_date": fake.date_between(start_date=date(2025, 1, 1), end_date=date(2025, 12, 1)),
        "days": days,
        "approved": np.random.choice([True, False], p=[0.9, 0.1])
    })

leave = pd.DataFrame(leave_records)

# Save files
departments.to_csv(OUTPUT_DIR / "departments.csv", index=False)
locations.to_csv(OUTPUT_DIR / "locations.csv", index=False)
employees.to_csv(OUTPUT_DIR / "employees.csv", index=False)
payroll.to_csv(OUTPUT_DIR / "payroll.csv", index=False)
training.to_csv(OUTPUT_DIR / "training.csv", index=False)
engagement.to_csv(OUTPUT_DIR / "engagement.csv", index=False)
leave.to_csv(OUTPUT_DIR / "leave.csv", index=False)

print("Synthetic HR data generated successfully.")
print(f"Employees: {len(employees)}")
print(f"Payroll rows: {len(payroll)}")
print(f"Training rows: {len(training)}")
print(f"Engagement rows: {len(engagement)}")
print(f"Leave rows: {len(leave)}")
