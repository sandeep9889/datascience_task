print("name: sandeep chouhan")
print("scholar no: 30203")
import csv
import numpy as np 
f=open("yellow_trip_data.csv","r",encoding="utf8")
taxi_list=list(csv.reader(f))

taxi_list=taxi_list[1:]

converted_taxi_list=[]
for row in taxi_list:
    converted_row=[]
    for item in row:
        if item=='':                         #Cleaning the data
            converted_row.append(float(0))   #Otherwise there will be an index error
        else:
            converted_row.append(float(item))
    converted_taxi_list.append(converted_row)

taxi=np.array(converted_taxi_list)
tip_bool=taxi[:,12]>10 #Changed the tip_amount from 50 to 10 as per the dataset
top_tips=taxi[tip_bool,5:14]
print(top_tips)