import matplotlib.pyplot as plt
import numpy as np

# Define x & Y ranges and tick interval for both axes
x_min, y_min, x_max, y_max = -5, -5, 5, 5
ticks_frequency = 1

# Create a figure and an axes object. Also set the face color. This will cover transparent margins.
fig, ax = plt.subplots(figsize=(10,10))

# Apply the ranges to the axes.
ax.set(xlim=(x_min-1, x_max+1), ylim=(y_min-1, y_max+1), aspect='equal')

# Set both axes to the zero position.
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')

# Hide the top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

x = np.linspace( start=-5 , stop=5 , num=150 )
y = np.linspace( start=-5 , stop=5 , num=150 )
 
a, b = np.meshgrid( x , y )
 
C = a ** 2 + b ** 2 - 15
 
ax.contour( a , b , C , [1])
ax.set_aspect( 1 )

# Display graph
plt.show()

