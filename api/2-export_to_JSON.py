#!/usr/bin/python3

import json
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

    tasks = [{"task": task['title'], "completed": task['completed'], "username": employee_name} for task in data]

    file_name = f"{employee_id}.json"
    with open(file_name, mode='w', encoding='utf-8') as jsonfile:
        json.dump({str(employee_id): tasks}, jsonfile, ensure_ascii=False, indent=4)

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
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            gather_data(employee_id)
        except ValueError:
            print("Error: Employee ID must be an integer.")
