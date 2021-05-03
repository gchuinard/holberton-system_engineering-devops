#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests


def main():
    url = 'https://jsonplaceholder.typicode.com/'
    employees = json.loads(requests.get(url + 'users').text)
    data = {}

    for employee in employees:
        urlId = url + 'todos/?userId=' + str(employee['id'])
        totalTasks = json.loads(requests.get(urlId).text)
        tasks = []
        for task in totalTasks:
            tmp = {'task': task['title'],
                   'completed': task['completed'],
                   'username': employee['username']}
            tasks.append(tmp)
        data[employee['id']] = tasks

    with open("todo_all_employees.json", "w") as outfile:
        json.dump(data, outfile)


if __name__ == "__main__":
    main()
