print("name: sandeep chouhan")
print("scholar no: 30203")
import csv
import numpy as np 
f=open("nyc_taxi.csv","r",encoding="utf8")
taxi_list=list(csv.reader(f))

taxi_list=taxi_list[1:]

fare_amount=list()
fee_amount=list()
for row in taxi_list:
    fare_amount.append(float(row[9]))
    fee_amount.append(float(row[10]))

fare_amount=np.array(fare_amount)
fee_amount=np.array(fee_amount)
fare_and_fee=fare_amount+fee_amount
print(fare_and_fee)
