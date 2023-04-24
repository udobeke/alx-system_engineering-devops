#!/usr/bin/python3

"""
This script uses the `json` module to write the tasks data fetched from an external REST API.
"""

import json
import sys
import requests
import csv


if __name__ == '__main__':
    import requests
    import json
    from sys import argv

    emp_id = argv[1]
    file_name = emp_id + '.json'
    total_todos = 0
    done_todos = 0
    done_todo_titles = []

    res = requests.get('https://jsonplaceholder.typicode.com/users/' +
                       emp_id)
    emp_username = res.json().get('username')

    res = requests.get('https://jsonplaceholder.typicode.com/users/' +
                       emp_id + '/todos')
    emp_todos = res.json()

    records = {str(emp_id): []}

    for item in emp_todos:
        total_todos += 1
        records[str(emp_id)].append({"task": item.get('title'),
                                     "completed": item.get("completed"),
                                     "username": emp_username})

    with open(file_name, 'w') as jsonfile:
        json.dump(records, jsonfile)
