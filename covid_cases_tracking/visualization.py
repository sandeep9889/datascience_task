import pandas as pd
import matplotlib.pyplot as plt
import csv
df =pd.read_csv('covid.csv')



# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# import csv

# f = open('covid.csv', 'r', encoding='utf8')

# covid_list = list(csv.reader(f))
# cases=covid_list[1:364]

# cases = np.array(cases)
# # present_cases = cases[:,4]
# deaths = cases[:,6]
# dates = cases[:,0]

# month = []
# for date in dates:
#     month.append(date[5:7])
# print(month)

# # converted_present_cases=[]
# # for i in present_cases:
# #     converted_present_cases.append(int(i))

# converted_deaths=[]
# for i in deaths:
#     converted_deaths.append(int(i))



# plt.title('New Reported Deaths By Month (Globally)')
# plt.plot(month, converted_deaths)
# plt.xlabel("month") #labeling x axis
# plt.ylabel("covid deaths") #labeling y axis
# plt.show()