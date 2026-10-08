import pandas as pd

students = pd.read_csv("student.csv")
print("first 5students:")
print(students.head())

average_mark = students["mark"].mean()
print("Average mark:", average_mark)

above_80_students = students[students["mark"] > 80]
print("\nStudents who scored above 80:")

print(above_80_students)
