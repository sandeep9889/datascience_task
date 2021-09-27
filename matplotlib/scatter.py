
# importing matplotlib module 
from matplotlib import pyplot as plt
  
month_number =[1,2,3,4,5,6,7]
new_deaths = [213,2729,37718,184064,143119,136073,165003]
  

  
# Function to plot scatter
plt.scatter(month_number, new_deaths)
  
# function to show the plot
plt.show()