import matplotlib.pyplot as plt

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
score = [22,43,23,12,32,45,75]

plt.plot(days , score, color="black")
plt.grid(True)
plt.ylabel("score")
plt.xlabel("days")
plt.title("matplotib.pyplot")
plt.show()
