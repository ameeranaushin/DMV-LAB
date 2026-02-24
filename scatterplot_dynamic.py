import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation

x_data = []
y_data = []

fig, ax = plt.subplots()

def update(frame):
   
    x_data.append(random.randint(0, 10))
    y_data.append(random.randint(0, 10))

    ax.clear()
    ax.scatter(x_data, y_data, color='blue')
    ax.set_title("Dynamic Scatter Plot")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")

ani = FuncAnimation(fig, update, interval=1000)

plt.show()
