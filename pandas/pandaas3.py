import pandas as pd
data = {"a":[1,2,3], "b":[5,8,4]}
df = pd.DataFrame(data)
B=df.drop("a",axis=1,inplace=True)
print(B)
df["c"] = df["a"]+df["b"]
print(df)
print(df.iloc[2]["c"])