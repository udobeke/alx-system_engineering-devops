#!/usr/bin/python3

"""cript to export data in the CSV format"""

import csv
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python3 export_to_CSV.py USER_ID")
    sys.exit(1)

user_id = sys.argv[1]
url = "https://jsonplaceholder.typicode.com"
user_url = url + "/users/" + user_id
tasks_url = url + "/todos?userId=" + user_id

# Fetch user data
user_data = requests.get(user_url).json()
username = user_data["username"]

# Fetch tasks data
tasks_data = requests.get(tasks_url).json()

# Write data to CSV file
file_name = user_id + ".csv"
with open(file_name, "w", newline="") as csvfile:
    fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for task in tasks_data:
        completed_status = "True" if task["completed"] else "False"
        writer.writerow(
            {
                "USER_ID": user_id,
                "USERNAME": username,
                "TASK_COMPLETED_STATUS": completed_status,
                "TASK_TITLE": task["title"],
            }
        )

print("Data has been exported to", file_name, "successfully!")

