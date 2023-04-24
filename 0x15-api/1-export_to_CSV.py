#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees and exporting data in CSV format"""


import csv
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = f"{base_url}/{employee_id}"

    response = requests.get(url)
    employee_name = response.json().get('username')

    todo_url = f"{url}/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    with open(f"{employee_id}.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        for task in tasks:
            task_status = 'True' if task.get('completed') else 'False'
            task_title = task.get('title')
            writer.writerow([employee_id, employee_name, task_status, task_title])
            print(f'"{employee_id}","{employee_name}","{task_status}","{task_title}"')
