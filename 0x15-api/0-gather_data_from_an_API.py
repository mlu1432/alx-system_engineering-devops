#!/usr/bin/python3
"""Gather data from an API and export to CSV"""
import csv
import sys

import requests

if len(sys.argv) != 2:
    print("Usage: ./1-export_to_CSV.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]

response = requests.get(
    f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
)

if response.status_code != 200:
    print("Error: Failed to retrieve TODO list")
    sys.exit(1)

todos = response.json()

response = requests.get(
    f"https://jsonplaceholder.typicode.com/users/{employee_id}"
)

if response.status_code != 200:
    print("Error: Failed to retrieve employee information")
    sys.exit(1)

employee = response.json()
employee_name = employee.get("name")

filename = f"{employee_id}.csv"

with open(filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    
    writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

    for todo in todos:
        task_completed_status = str(todo.get("completed"))
        task_title = todo.get("title")
        writer.writerow([employee_id, employee_name, task_completed_status, task_title])

print(f"Data saved to {filename} successfully")
