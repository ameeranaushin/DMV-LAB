import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation

labels = ['A', 'B', 'C', 'D']

fig, ax = plt.subplots()

def update(frame):
    ax.clear()
    sizes = [random.randint(10, 50) for _ in labels]
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.set_title("Live Updating Pie Chart")

ani = FuncAnimation(fig, update, interval=1000)
plt.show()
