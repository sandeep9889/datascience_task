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

drop_location=taxi[:,6]
jfk=drop_location==48
jfk=taxi[jfk,6]
jfk_count=len(jfk)


drop_location=taxi[:,6]
laguardia=drop_location==79
laguardia=taxi[laguardia,6]
laguardia_count=len(laguardia)

drop_location=taxi[:,6]
newark=drop_location==114
newark=taxi[newark,6]
newark_count=len(newark)

print("JFK:",jfk_count)
print("LaGuardia:",laguardia_count)
print("Newark:",newark_count)

max_drop=max(newark_count,laguardia_count,jfk_count)

dic=dict({"JFK:":jfk_count,"LaGuardia":laguardia_count,"Newark":newark_count})
for ap,count in dic.items():
    if count==max_drop:
        print(ap+' has the most dropoffs:',count)