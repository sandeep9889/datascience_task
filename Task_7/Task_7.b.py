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
    for item in row:
        converted_row.append(float(item))
    converted_taxi_list.append(converted_row)

taxi=np.array(converted_taxi_list)

trip_distance = taxi [:,7]
print(trip_distance)

trip_length_seconds = taxi [:,8]
trip_length_hours = trip_length_seconds/3600 
print(trip_length_hours)

trip_mph = trip_distance / trip_length_hours

print(trip_mph)
print(trip_mph.min())
print(trip_mph.max())