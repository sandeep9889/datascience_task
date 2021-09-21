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
            converted_row.append(0.00)   #Otherwise there will be an index error
        else:
            converted_row.append(float(item))
    converted_taxi_list.append(converted_row)

taxi=np.array(converted_taxi_list)
taxi_copy=taxi.copy()
total_amount=taxi_copy[:,13]

total_bool=total_amount<0

print(taxi_copy[total_bool,13])
taxi_copy[total_bool,13]=0
print(taxi_copy[total_bool,13])

