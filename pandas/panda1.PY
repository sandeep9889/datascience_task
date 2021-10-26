import pandas as pd
data = {"height":[133,120,180,100], "age":[20,41,52,23]}  #here we have seprated height and age
df= pd.DataFrame(data)
print(df.height)