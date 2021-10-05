import pandas as pd






df=pd.read_csv('export.csv')

print(df.to_string())

df1=df.dropna()


dr1=df.fillna(130,inplace=True)


print(df1.to_string())

