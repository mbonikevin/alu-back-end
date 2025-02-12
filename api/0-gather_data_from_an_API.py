#!/usr/bin/python3

import sys  # system operations
import requests  # HTTP requests

def gather_data(employee_id):  # gather task data
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"  # user todo URL
    response = requests.get(url)  # send GET request
    if response.status_code != 200:  # check response status
        print("Error: Unable to fetch data")  # handle error
        return

    data = response.json()  # parse JSON response
    completed_tasks = [task['title'] for task in data if task['completed']]  # filter completed tasks
    total_tasks = len(data)  # total number of tasks
    completed_count = len(completed_tasks)  # completed task count

    if total_tasks == 0:  # check if no tasks
        print(f"Employee {employee_name(employee_id)} is done with tasks(0/0):")  # no tasks message
    else:
        print(f"Employee {employee_name(employee_id)} is done with tasks({completed_count}/{total_tasks}):")  # task status
        for task in completed_tasks:  # loop through completed tasks
            print(f"\t {task}")  # print task

def employee_name(employee_id):  # fetch employee name
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"  # user URL
    response = requests.get(url)  # send GET request
    if response.status_code == 200:  # check response status
        user_data = response.json()  # parse JSON response
        return user_data.get('name', 'Unknown Employee')  # return employee name
    else:
        return 'Unknown Employee'  # default name

if __name__ == "__main__":  # main script execution
    if len(sys.argv) != 2:  # check argument count
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")  # print usage
    else:
        try:
            employee_id = int(sys.argv[1])  # parse employee ID
            gather_data(employee_id)  # gather and display data
        except ValueError:  # handle invalid ID
            print("Error: Employee ID must be an integer.")  # invalid ID message
