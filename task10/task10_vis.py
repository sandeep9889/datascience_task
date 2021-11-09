import pandas as pd
import numpy as np
from matplotlib import colors, pyplot as plt

df = pd.read_csv("2015.csv")
df1 = pd.DataFrame(df)
# print(df.to_string)
plt.plot(df['Happiness Score'],df['Country'],label='score',color ='green')
plt.title("happiness Score")
plt.xlabel = "score"
plt.show()