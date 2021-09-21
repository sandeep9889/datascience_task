print("name: sandeep chouhan")
print("scholar no: 30203")
import numpy as np
taxi=np.genfromtxt("nyc_taxi.csv",delimiter=',')
(r,c)=taxi.shape
print("Taxi shape: ",(r,c))
print(type(taxi))
print(type(taxi.shape))