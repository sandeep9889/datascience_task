import csv
import numpy as np 
fi=open("yellow_trip_data.csv","r",encoding="utf8")
taxi_list=list(csv.reader(fi))

dic=dict()

for row in taxi_list[1:]:
    key=row[6]
    if row[6] not in dic.keys():
        dic[key]=1
    else:
        dic[key]+=1

print(dic['48'])
print(dic['79'])
print(dic['114'])







































