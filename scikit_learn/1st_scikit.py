from scipy.sparse.construct import random
from sklearn import model_selection
from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split
X = boston[['RM']]
Y =boston[['MEDV']]
X_test,X_train,Y_train,Y_test = train_test_split( X , Y ,test_size =0.3 , random_state =1)
model = LinearRegression()
model.fit(X_train,Y_train) #to train the data
model.intercept_.__round__(2)
model.coef_.round(2)
print(X_train.shape)