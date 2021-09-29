
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

from pandas.core.frame import DataFrame
df =pd.read_csv('covid.csv')
# f = open("covid.csv", "r" ,encoding="utf8")
# df = list(csv.reader(f))
who_time_series=DataFrame(df)
# who_time_series = np.array(df1)
# who_time_series = who_time_series[1:]
# print(who_time_series)

france = who_time_series[who_time_series["Country"]== "France"]
france_june = who_time_series[who_time_series["Date_reported"] == france["Date_reported"[5:7]]]
plt.plot(france_june,france["Cumulative_cases"],label ="france")
plt.show()
#2019-07-01

# print(france)

