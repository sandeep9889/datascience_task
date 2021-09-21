print("name: sandeep chouhan")
print("scholar no: 30203")
import csv
import numpy as np 
fi=open("yellow_trip_data.csv","r",encoding="utf8")
taxi_list=list(csv.reader(fi))

fo=open("taxi_modified.csv","w",encoding="utf8")
writer=csv.writer(fo)

taxi_list[0].append("dropped_airport")

writer.writerow(taxi_list[0])

for row in taxi_list[1:]:
    converted_row=[]
    for item in row:
        if item=='':                         #Cleaning the data
            converted_row.append(0.00)   #Otherwise there will be an index error
        else:
            converted_row.append(float(item))
    if converted_row[5]==48 or converted_row[5]==79 or converted_row[5]==114:
        #JFK Airport: 48, LaGuardia Airport: 79, Newark Airport: 114
        converted_row.append(1)
    else:
        converted_row.append(0)
    writer.writerow(converted_row)

