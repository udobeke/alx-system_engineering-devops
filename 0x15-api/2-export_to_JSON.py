#!/usr/bin/python3

"""
This script uses the `json` module to write the tasks data fetched from an external REST API.
"""

import json
import sys
import requests
import csv


# Function to filter tasks by username
def filter_tasks_by_username(tasks, username):
    filtered_tasks = []
    for task in tasks:
        if task["username"] == username:
            filtered_tasks.append(task)
    return filtered_tasks


# Function to export tasks to JSON
def export_tasks_to_json(user_id):
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = f"{base_url}/{user_id}"

    response = requests.get(url)
    employee_name = response.json().get('username')

    todo_url = f"{url}/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    filtered_tasks = filter_tasks_by_username(tasks, employee_name)
    data = {user_id: filtered_tasks}
    filename = f"{user_id}.json"
    with open(filename, "w") as json_file:
        json.dump(data, json_file)


# Check if user ID is provided as a command line argument
if len(sys.argv) > 1:
    user_id = sys.argv[1]
    export_tasks_to_json(user_id)
    print(f"Tasks for User ID '{user_id}' exported to '{user_id}.json' in JSON format.")
else:
    print("Please provide a user ID as a command line argument.")
