#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]

# Use f-strings for better readability
response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

# Split long lines for better readability
if response.status_code != 200:
    print("Error: Failed to retrieve TODO list")
    sys.exit(1)

todos = response.json()

response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")

if response.status_code != 200:
    print("Error: Failed to retrieve employee information")
    sys.exit(1)

employee = response.json()
# Correct employee_name to use "name" instead of "username"
employee_name = employee.get("name")

completed_tasks = [todo for todo in todos if todo.get("completed")]
number_of_completed_tasks = len(completed_tasks)
total_number_of_tasks = len(todos)

# Adjust the output messages to match the expected format
print(f"Employee {employee_name} is done with tasks ({number_of_completed_tasks}/{total_number_of_tasks}):")
for task in completed_tasks:
    print(f"\t{task.get('title')}")

# Add a newline for better separation of output
print()
