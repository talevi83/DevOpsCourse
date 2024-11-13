import matplotlib.pyplot as plt
import math

# Generate data
x = [i for i in range(0, 11)]   # x values from 0 to 10
y = [math.sin(i) for i in x]    # y values as the sine of each x point

# Create the plot
plt.figure(figsize=(10, 5))  # Set the figure size
plt.plot(x, y, label='Sine Wave', color='blue')  # Plot the data

# Add titles and labels
plt.title('Basic Line Plot of Sine Function')
plt.xlabel('X values')
plt.ylabel('Y values (sin(x))')

# Add a legend
plt.legend()

# Show grid
plt.grid()

# Show the plot
plt.show()