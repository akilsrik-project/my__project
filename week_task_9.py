with open("student.txt", "w") as file:

    file.write("suresh - 85\n")
    file.write("ramesh - 90\n")
    file.write("akhil - 95\n")

with open("student.txt", "r") as file:
    content = file.read()
    print("student details:")
    print(content)