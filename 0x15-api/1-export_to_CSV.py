#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress
and export data in the CSV format.
"""
import csv
import json
import requests
from sys import argv


def main():
    employeeId = argv[1]
    userData = requests.get('https://jsonplaceholder.typicode.com/users?id={}'
                            .format(employeeId)).json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(employeeId)).json()
    username = userData[0]['username']

    with open(str(employeeId) + ".csv", mode="w") as employeeF:
        fWrite = csv.writer(employeeF, quoting=csv.QUOTE_ALL)

    for task in tasks:
        fWrite.writerow([task['userId'], username,
                         task['completed'], task['title']])


if __name__ == "__main__":
    main()
