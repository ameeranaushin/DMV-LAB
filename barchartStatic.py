import matplotlib.pyplot as plt

# Sample data
categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 24, 36, 18, 12]

# Create bar chart
plt.bar(categories, values, color='skyblue')

# Add labels and title
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Static Bar Chart")

# Show the plot
plt.show()