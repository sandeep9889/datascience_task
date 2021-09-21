print("name: sandeep chouhan")
print("scholar no: 30203")
import csv
import numpy as np 
taxi=np.genfromtxt("nyc_taxi.csv",delimiter=',')
taxi=taxi[1:]

cleaned_taxi=list()
for _ in range(len(taxi)):
    trip_mph=3600*taxi[_,7]/taxi[_,8]
    if trip_mph<100:
        cleaned_taxi.append(taxi[_])

cleaned_taxi=np.array(cleaned_taxi)

mean_distance=cleaned_taxi[:,7].sum()/len(cleaned_taxi)
print("Mean distance:",mean_distance,"\n")

mean_length=cleaned_taxi[:,8].sum()/len(cleaned_taxi)
print("Mean length:",mean_length,"\n")

mean_total_amount=cleaned_taxi[:,13].sum()/len(cleaned_taxi)
print("Mean total amount:",mean_total_amount,"\n")
