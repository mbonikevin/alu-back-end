#!/usr/bin/python3

import csv
import sys
import requests

def gather_data(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Unable to fetch data")
        return

    data = response.json()
    employee_name = get_employee_name(employee_id)

    tasks = [(employee_id, employee_name, task['completed'], task['title']) for task in data]

    file_name = f"{employee_id}.csv"
    with open(file_name, mode='w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        csv_writer.writerows(tasks)

    print(f"Data for employee {employee_name} has been exported to {file_name}")

def get_employee_name(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    if response.status_code == 200:
        user_data = response.json()
        return user_data.get('username', 'Unknown User')
    else:
        return 'Unknown User'

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            gather_data(employee_id)
        except ValueError:
            print("Error: Employee ID must be an integer.")
