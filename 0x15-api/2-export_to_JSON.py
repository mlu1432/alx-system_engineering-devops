#!/usr/bin/python3
"""Gather data from an API and export to JSON"""
import requests
import json
import sys

if len(sys.argv) != 2:
    print("Usage: ./2-export_to_JSON.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]

user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
if user_response.status_code != 200:
    print("Error: Failed to retrieve employee information")
    sys.exit(1)
user = user_response.json()
username = user.get("username")

todos_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
if todos_response.status_code != 200:
    print("Error: Failed to retrieve TODO list")
    sys.exit(1)
todos = todos_response.json()

task_list = []
for todo in todos:
    task = {"task": todo.get("title"), "completed": todo.get("completed"), "username": username}
    task_list.append(task)
task_dict = {employee_id: task_list}

filename = f"{employee_id}.json"
with open(filename, "w") as jsonfile:
    json.dump(task_dict, jsonfile)

print(f"Data saved to {filename} successfully")
