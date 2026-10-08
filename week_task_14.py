import matplotlib.pyplot as plt

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
sales = [1000, 1200, 1500, 1800, 2000, 2200, 2500, 2700, 3000, 3200, 3500, 4000]

plt.plot(months, sales)
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.show()


