#!/usr/bin/python3
"""Gather data from an API"""
import json
import requests
import sys


def main():
    url = 'https://jsonplaceholder.typicode.com/'
    user = sys.argv[1]
    urlId = url + 'users/?id=' + user
    employee = json.loads(requests.get(urlId).text)
    urlId = url + 'todos/?userId=' + user
    totalTasks = json.loads(requests.get(urlId).text)
    tasks = []
    data = {user: tasks}

    for task in totalTasks:
        tmp = {'task': task['title'],
               'completed': task['completed'],
               'username': employee[0]['username']}
        tasks.append(tmp)
    with open(user + ".json", "w") as outfile:
        json.dump(data, outfile)


if __name__ == "__main__":
    main()
