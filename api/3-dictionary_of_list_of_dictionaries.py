#!/usr/bin/python3

"""
This script fetches all tasks from a public API, processes the tasks by user, 
and saves the processed data to a JSON file. The data includes the username, 
task title, and completion status, grouped by user.
"""

import json
import requests


def fetch_todos():
    """
    Fetches all tasks (todos) from the API.
    Returns the tasks in JSON format if successful, otherwise returns an empty list.
    """
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Unable to fetch data")
        return []
    return response.json()


def process_data(todos):
    """
    Processes the fetched todos and organizes them by user ID.
    Returns a dictionary where each key is a user ID and the value is a list of tasks.
    """
    tasks_by_user = {}

    for todo in todos:
        user_id = str(todo["userId"])
        task_info = {
            "username": todo["username"],
            "task": todo["title"],
            "completed": todo["completed"]
        }

        if user_id not in tasks_by_user:
            tasks_by_user[user_id] = []

        tasks_by_user[user_id].append(task_info)

    return tasks_by_user


def save_to_json(tasks_by_user):
    """
    Saves the processed data (tasks by user) to a JSON file.
    Writes to a file named 'todo_all_employees.json' with formatted indentation.
    """
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(tasks_by_user, json_file, indent=4)

    print("Data has been written to todo_all_employees.json")

if __name__ == "__main__":
    """
    Main script execution.
    Fetches tasks, processes them, and saves them to a JSON file.
    """
    todos = fetch_todos()
    if todos:
        tasks_by_user = process_data(todos)
        save_to_json(tasks_by_user)
