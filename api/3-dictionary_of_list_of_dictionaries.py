#!/usr/bin/python3

import json
import requests

def fetch_todos():
    # We'll fetch the data from the API
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Unable to fetch data")
        return []
    return response.json()

def process_data(todos):
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
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(tasks_by_user, json_file, indent=4)

    print("Data has been written to todo_all_employees.json")

if __name__ == "__main__":
    todos = fetch_todos()
    if todos:
        tasks_by_user = process_data(todos)
        save_to_json(tasks_by_user)
