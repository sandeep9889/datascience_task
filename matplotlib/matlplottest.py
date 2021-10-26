from matplotlib import colors
import matplotlib.pyplot as plt
month_number =[1,2,3,4,5,6,7]
new_deaths = [213,2729,37718,184064,143119,136073,165003]
plt.plot(month_number, new_deaths, color='red', label ='India')
plt.ticklabel_format(axis='y',style="plain")
plt.title("new reported deaths global")
plt.xlabel("month number")
plt.ylabel("no of deaths")
# plt.show()