#!/usr/bin/python3

"""cript to export data in the CSV format"""

import csv
import requests
import sys

if __name__ == '__main__':
    import requests
    from sys import argv
    emp_id = argv[1]
    file_name = emp_id + '.csv'
    total_todos = 0
    done_todos = 0
    done_todos_titles = []

    res = requests.get(
                   'https://jsonplaceholder.typicode.com/users/' +
                   emp_id)
    emp_name = res.json().get('username')

    res = requests.get(
                   'https://jsonplaceholder.typicode.com/users/' +
                   emp_id + '/todos')
    emp_todos = res.json()

    with open(file_name, 'w') as csvfile:
        for item in emp_todos:
            total_todos += 1
            csvfile.write(
                    '"{}","{}","{}","{}"\n'.format(
                                            item.get('userId'),
                                            emp_name,
                                            item.get('completed'),
                                            item.get('title')
                                            ))
