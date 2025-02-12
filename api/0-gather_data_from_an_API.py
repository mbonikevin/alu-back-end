#!/usr/bin/python3

"""
This script fetches tasks for a given employee from the API.
It takes an employee ID as a command-line argument.
Displays completed tasks for the employee and their total task count.
"""

import requests  # HTTP requests
import sys  # system operations


def gather_data(employee_id):
    """Fetch and display tasks for an employee."""
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error: Unable to fetch data")
        return

    data = response.json()
    completed_tasks = [task['title'] for task in data if task['completed']]
    total_tasks = len(data)
    completed_count = len(completed_tasks)

    if total_tasks == 0:
        print(f"Employee {employee_name(employee_id)} is done with tasks("
              f"0/0):")
    else:
        print(f"Employee {employee_name(employee_id)} is done with tasks("
              f"{completed_count}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t {task}")


def employee_name(employee_id):
    """Fetch employee name using their ID."""
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)

    if response.status_code == 200:
        user_data = response.json()
        return user_data.get('name', 'Unknown Employee')
    else:
        return 'Unknown Employee'


if __name__ == "__main__":
    """Main script execution."""
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            gather_data(employee_id)
        except ValueError:
            print("Error: Employee ID must be an integer.")
