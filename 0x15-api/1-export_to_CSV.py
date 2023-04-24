#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees and exporting data in CSV format"""

import csv
import requests
import sys

if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = f"{baseUrl}/{employeeId}"

    response = requests.get(url)
    employeeName = response.json().get('username')

    todoUrl = f"{url}/todos"
    response = requests.get(todoUrl)
    tasks = response.json()

    with open(f"{employeeId}.csv", mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(
            ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])

        for task in tasks:
            task_status = 'True' if task.get('completed') else 'False'
            task_title = task.get('title')
            writer.writerow(
                [employeeId, employeeName, task_status, task_title])
            print(f'"{employeeId}","{employeeName}",'
                  f'"{task_status}","{task_title}"')
