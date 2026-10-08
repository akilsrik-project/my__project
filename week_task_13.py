import numpy as np

marks = np.array([85, 90, 95, 87, 75, 88, 92, 78, 84, 91])

mean_mark = np.mean(marks)
maximum_mark = np.max(marks)
minimum_mark = np.min(marks)

above_80_marks = marks[marks > 80]

print("marks:", marks)
print("Mean mark:", mean_mark)
print("Maximum mark:", maximum_mark)
print("Minimum mark:", minimum_mark)
print("marks greater than 80:", above_80_marks)

