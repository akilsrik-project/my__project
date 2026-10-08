[
    {
        "id": 1,
        "name": "arjun",
        "department": "mecchanical"
    },
    {
        "id": 2,
        "name": "suresh",
        "department": "civil"
    },
    {
        "id": 3,
        "name": "ramesh",
        "department": "electrical"
    }
]


import json

with open("students.json", "r") as file:
    student = json.load(file)

    for student in student:
        print("name:", student["name"])
        print("department:", student["department"])
        print()
        