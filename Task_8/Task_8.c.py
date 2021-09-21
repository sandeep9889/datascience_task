print("name: sandeep chouhan")
print("scholar no: 30203")
import numpy as np
taxi=np.genfromtxt("nyc_taxi.csv",delimiter=',')
taxi=taxi[1:,]
(r,c)=taxi.shape
print(r,c)