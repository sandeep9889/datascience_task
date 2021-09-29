
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
print(france)

