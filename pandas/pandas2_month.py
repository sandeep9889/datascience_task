import pandas as pd
data = {"jan":[255,260,265,270,275],"feb":[280,285,290,295,300],"march":[355,360,365,370,375],"aprail":[380,385,390,395,400]}
df = pd.DataFrame(data)
print(df.jan[0])