#!/usr/bin/python3
"""Gather data from an API and export to JSON"""
import json

import requests

user_response = requests.get("https://jsonplaceholder.typicode.com/users")
user = user_response.json()
todos_response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = todos_response.json()

all_tasks = {}
for user in user:
    user_id = user.get("id")
    task_list = []
    for todo in todos:
        if user_id == todo.get("userId"):
            task = {"username": user.get("username"),
                    "task": todo.get("title"),
                    "completed": todo.get("completed")}
            task_list.append(task)
    all_tasks[user_id] = task_list

filename = "todo_all_employees.json"
with open(filename, "w") as jsonfile:
    json.dump(all_tasks, jsonfile)

print(f"Data saved to {filename} successfully")
