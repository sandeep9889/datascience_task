
# importing matplotlib module 
from matplotlib import pyplot as plt
  
# x-axis values
month_name = [1,2,3,4,5,6,7]
  
# Y-axis values
death_cases = [213,2729,37718,184064,143119,136073,165003 ]
  
# Function to plot the bar
plt.bar(month_name,death_cases)
  
# function to show the plot
plt.show()