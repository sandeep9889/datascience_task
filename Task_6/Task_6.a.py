print("name: sandeep chouhan")
print("scholar no: 30203")
import csv
import numpy as np 
f=open("nyc_taxi_new.csv","r",encoding="utf8")
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
february_bool=taxi[:,1]==2
february=taxi[february_bool,1]
february_rides=february.shape[0]
print(february_rides)