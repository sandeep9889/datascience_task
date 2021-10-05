
from matplotlib import colors
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import re

from pandas.core.frame import DataFrame
from pandas.tseries.offsets import MonthBegin
df =pd.read_csv('covid.csv')
# f = open("covid.csv", "r" ,encoding="utf8")
# df = list(csv.reader(f))
who_time_series=DataFrame(df)
# who_time_series = np.array(df1)
# who_time_series = who_time_series[1:]
# print(who_time_series)

france = who_time_series[who_time_series["Country"]== "France"]
# france_june = who_time_series[who_time_series["Date_reported"] == france["Date_reported"[5:7]]]
france["Date_reported"]=pd.to_datetime(france["Date_reported"])
Mon=france[france["Date_reported"].dt.month == 7]
da=Mon[Mon["Date_reported"]]
print(da[0: ,5:7])
# print("da")

# print(france["Date_reported"])

plt.plot(,france["Cumulative_cases"],label ="france",color = "orange")


itlay = who_time_series[who_time_series["Country"]== "Itlay"]
itlay_june = who_time_series[who_time_series["Date_reported"] == itlay["Date_reported"[5:7]]]
plt.plot(itlay_june,itlay["Cumulative_cases"],label ="france",color = "red")


Uganda = who_time_series[who_time_series["Country"]== "Uganda"]
Uganda_june = who_time_series[who_time_series["Date_reported"] == Uganda["Date_reported"[5:7]]]
plt.plot(Uganda_june,Uganda["Cumulative_cases"],label ="france",color = "black")



plt.title("covid cases tracking ")
plt.xlabel("dates of july")
plt.ylabel("cases")

plt.legend()
plt.show()
# 2019-07-01

print(france)

