#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 todo_list.py EMPLOYEE_ID")
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = base_url + "/" + employee_id

    try:
        response = requests.get(url)
        response.raise_for_status()
        employee_name = response.json().get('name')
    except requests.exceptions.HTTPError:
        print("Invalid employee ID provided.")
        sys.exit(1)
    except requests.exceptions.RequestException:
        print("An error occurred while accessing the API.")
        sys.exit(1)

    todo_url = url + "/todos"

    try:
        response = requests.get(todo_url)
        response.raise_for_status()
        tasks = response.json()
        done_tasks = [task for task in tasks if task['completed']]
    except requests.exceptions.HTTPError:
        print("An error occurred while accessing the employee's TODO list.")
        sys.exit(1)
    except requests.exceptions.RequestException:
        print("An error occurred while accessing the API.")
        sys.exit(1)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, len(done_tasks), len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
