print("name: sandeep chouhan")
print("scholar no: 30203")
import csv
import numpy as np
f=open("nyc_taxi.csv","r",encoding="utf8")
taxi_list=list(csv.reader(f))

taxi_list=taxi_list[1:]

converted_taxi_list=[]
for row in taxi_list:
    converted_row=[]
    for item in row[9:14]:
        converted_row.append(float(item))
    converted_taxi_list.append(converted_row)

taxi=np.array(converted_taxi_list)
fare_sums=[]
fare_components=taxi[0:5,0:4]
for _ in range(len(fare_components)):
    print("Row",_+1,":",fare_components[_,:].sum()==taxi[_,-1])
    fare_sums.append(fare_components[_,:].sum())

fare_totals=taxi[0:,-1]
print(fare_totals,fare_sums)