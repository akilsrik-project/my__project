student = [
    {"id": 1, "name": "Alice", "age": 20, "grade": 85},
    {"id": 2, "name": "Bob", "age": 22, "grade": 90},
    {"id": 3, "name": "Charlie", "age": 21, "grade": 78}

]

print("Student List:")
for s in student:
    print(student)

    student_id = int(input("Enter student Id: "))

    found = False
    for s in student:
        if s["id"] == student_id:
            print(f"Student Found: Name: {s['name']}, Age: {s['age']}, Grade: {s['grade']}")
            found = True
            break

    if not found:
        print("Student not found.")
        