#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees and exporting data in CSV format"""

import csv
import requests
import sys


def main():
    """Main function to fetch and display employee TODO list progress and export data in CSV"""

    if len(sys.argv) != 2:
        print("Usage: python3 todo_list.py EMPLOYEE_ID")
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = "{}/{}".format(base_url, employee_id)

    try:
        response = requests.get(url)
        response.raise_for_status()
        employee_name = response.json().get('name')
    except requests.exceptions.RequestException as e:
        print("An error occurred while accessing the API. Error: {}".format(e))
        sys.exit(1)

    todo_url = "{}/todos".format(url)

    try:
        response = requests.get(todo_url)
        response.raise_for_status()
        tasks = response.json()
        done_tasks = [task for task in tasks if task['completed']]
    except requests.exceptions.RequestException as e:
        print("An error occurred while accessing the employee's TODO list. Error: {}".format(e))
        sys.exit(1)

    num_done_tasks = len(done_tasks)
    num_total_tasks = len(tasks)

    print("Employee {} is done with tasks({}/{}):".format(employee_name, num_done_tasks, num_total_tasks))

    for task in done_tasks:
        print("\t{}".format(task['title']))

    # Export data in CSV format
    csv_filename = "{}.csv".format(employee_id)
    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': task['completed'],
                'TASK_TITLE': task['title']
            })

    print("User ID and Username: OK")
    print("Data exported to {} in CSV format.".format(csv_filename))


if __name__ == '__main__':
    main()
