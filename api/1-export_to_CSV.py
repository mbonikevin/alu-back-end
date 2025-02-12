#!/usr/bin/python3

"""
This script fetches tasks for a given employee from the API
and exports them to a CSV file. The employee ID is passed
as a command-line argument. The script retrieves tasks and
writes them to a CSV with columns for user ID, username,
task completion status, and task title.
"""

import csv
import requests
import sys


def gather_data(employee_id):
    """fetches tasks for a given employee and saves to CSV"""
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Unable to fetch data")
        return

    data = response.json()
    print(f"Total tasks fetched: {len(data)}")

    employee_name = get_employee_name(employee_id)

    tasks = [
        (employee_id, employee_name, task['completed'], task['title'])
        for task in data
    ]

    print(f"Tasks to write to CSV: {len(tasks)}")

    file_name = f"{employee_id}.csv"
    with open(file_name, mode='w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile, quotechar='"',
                                quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["USER_ID", "USERNAME",
                             "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        csv_writer.writerows(tasks)

    print(
        f"Data for employee {employee_name} has been exported to {file_name}"
    )


def get_employee_name(employee_id):
    """fetches the name of an employee from the API"""
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    if response.status_code == 200:
        user_data = response.json()
        return user_data.get('username', 'Unknown User')
    else:
        return 'Unknown User'


if __name__ == "__main__":
    """main function to process command-line arguments and execute gathering"""
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            gather_data(employee_id)
        except ValueError:
            print("Error: Employee ID must be an integer.")
