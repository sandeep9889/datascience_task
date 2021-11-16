import matplotlib.pyplot as plt
import numpy  as np
from numpy.core.fromnumeric import mean
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error


diabetes = datasets.load_diabetes()
# (['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module'])

#  to know the information
# print(diabetes.DESCR)

diabetes_X =np.array[[1],[2],[3]]
# print(diabetes_X)

diabetes_X_train = diabetes_X
diabetes_X_test = diabetes_X

diabetes_Y_train =np.array([3,2,4])
diabetes_Y_test =np.array([3,2,4])


model = linear_model.LinearRegression()
model.fit(diabetes_X_train,diabetes_Y_train)

diabetes_Y_predicted=model.predict(diabetes_X_test)

print(" mean square error is", mean_squared_error(diabetes_Y_test,diabetes_Y_predicted))

print("weights:",model.coef_)
print("intercept :",model.intercept_)

plt.scatter(diabetes_X_test,diabetes_Y_test)
plt.plot(diabetes_X_test,diabetes_Y_predicted)

plt.show()


#  mean square error is 2561.3204277283867
# weights: [941.43097333]
# intercept : 153.39713623331698