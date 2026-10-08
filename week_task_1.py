name = input("enter student name: ")

mark1 = int(input("enter mark 1: "))
mark2 = int(input("enter mark 2: "))
mark3 = int(input("enter mark 3: "))

total = mark1 + mark2 + mark3
average = total / 3

print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)

if average >= 50:
    print("result: pass")
else:
    print("result: fail")

    