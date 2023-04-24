#!/usr/bin/python3

"""
This Python script demonstrates how to filter tasks by username from a list of tasks
and export the filtered tasks to a JSON file. The script uses the `json` module to 
write the tasks data to a JSON file with the filename being the user ID, and the format
of the JSON file follows the requirements provided.
"""

import json
import sys


# Sample data
tasks = [
    {"task": "Task 1", "completed": True, "username": "user1"},
    {"task": "Task 2", "completed": False, "username": "user2"},
    {"task": "Task 3", "completed": True, "username": "user1"},
    {"task": "Task 4", "completed": False, "username": "user1"},
    {"task": "Task 5", "completed": True, "username": "user2"}
]


# Function to filter tasks by username
def filter_tasks_by_username(tasks, username):
    filtered_tasks = []
    for task in tasks:
        if task["username"] == username:
            filtered_tasks.append(task)
    return filtered_tasks


# Function to export tasks to JSON
def export_tasks_to_json(tasks, user_id):
    filtered_tasks = filter_tasks_by_username(tasks, user_id)
    data = {user_id: filtered_tasks}
    filename = "{}.json".format(user_id)
    with open(filename, "w") as json_file:
        json.dump(data, json_file)


# Check if user ID is provided as a command line argument
if len(sys.argv) > 1:
    user_id = sys.argv[1]
    export_tasks_to_json(tasks, user_id)
    print("Tasks for User ID '{}' exported to '{}.json' in JSON format.".format(user_id, user_id))
else:
    print("Please provide a user ID as a command line argument.")
