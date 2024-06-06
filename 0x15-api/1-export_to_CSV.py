#!/usr/bin/python3
"""
This script gathers data from a REST API for a given employee ID and exports
information about the employee's TODO list to a CSV file.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    session = requests.Session()

    todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

    try:
        todos_response = session.get(todos_url)
        todos_response.raise_for_status()
        todos = todos_response.json()

        user_response = session.get(user_url)
        user_response.raise_for_status()
        user = user_response.json()
        username = user.get('username')

        file_csv = f"{employee_id}.csv"

        with open(file_csv, "w", newline='') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for task in todos:
                writer.writerow([employee_id, username, task.get('completed'), task.get('title')])

        print(f"Data exported to {file_csv}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
