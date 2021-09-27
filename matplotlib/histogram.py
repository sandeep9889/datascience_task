# importing matplotlib module 
from matplotlib import pyplot as plt
  
# Y-axis values
death_cases= [213,2729,37718,184064,143119,136073,165003]
  
# Function to plot histogram
plt.hist(death_cases)
  
# Function to show the plot
plt.show()