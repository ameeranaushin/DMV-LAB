import matplotlib.pyplot as plt
import math

n = int(input("Enter number of vertices (>=3): "))

if n < 3:
    print("Number of vertices must be at least 3.")
    exit()

points = []
for i in range(n):
    angle = 2 * math.pi * i / n
    x = math.cos(angle)
    y = math.sin(angle)
    points.append((x, y))

for i, (x, y) in enumerate(points):
    plt.scatter(x, y)
    plt.text(x, y, f" {i+1}")

for i in range(n):
    for j in range(i + 1, n):
        x_values = [points[i][0], points[j][0]]
        y_values = [points[i][1], points[j][1]]
        plt.plot(x_values, y_values, 'b-')

plt.title(f"Complete Graph K{n}")
plt.gca().set_aspect('equal', adjustable='box')
plt.show()