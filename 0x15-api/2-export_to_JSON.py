#!/usr/bin/python3
"""
This script gathers data from a REST API for a given employee ID and exports
information about the employee's TODO list to a JSON file.
"""
import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        session = requests.Session()

        todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
        user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

        todos_response = session.get(todos_url)
        todos_response.raise_for_status()
        todos = todos_response.json()

        user_response = session.get(user_url)
        user_response.raise_for_status()
        user = user_response.json()
        username = user.get('username')

        tasks = [
            {"task": task.get('title'), "completed": task.get('completed'), "username": username}
            for task in todos
        ]

        data = {employee_id: tasks}

        file_json = f"{employee_id}.json"
        with open(file_json, "w") as jsonfile:
            json.dump(data, jsonfile)

        print(f"Data exported to {file_json}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
