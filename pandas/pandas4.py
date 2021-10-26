#we have indexing
import pandas as pd
data = {"weight":[50,75,55,60],"height":[178,190,175,150]}
df = pd.DataFrame(data,index=["randy","rem","jhon","cena"])
# df.head()
print(df)
san=df.groupby(data["weight"])
print(san)
