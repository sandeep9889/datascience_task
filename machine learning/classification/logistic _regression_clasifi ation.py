# logistic regression clasification 
"""
i think you have doubt in the name because here is clasifier but also name is regression 
because in regression it shows a number as output


sa as well as same as linearregression it show aslo a number as probablity
first a fall it shows probability and then it shows clasification"""

""" 
#- class:
                 - Iris-Setosa  ---0
                 - Iris-Versicolour ----1
                 - Iris-Virginica ---2"""



"""
#features
        - sepal length in cm
        - sepal width in cm
        - petal length in cm
        - petal width in cm"""
# train a logistic regresion classifier whether iris is iris -virginica or not 
from sklearn import datasets
import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
iris = datasets.load_iris()
# print(list(iris.keys()))
# print(iris['data'])
# print(iris['target'])
# print(iris['DESCR'])
# print(iris['data'].shape)
'''
we will try to learn machine with ine data  data like  ==petal lenghth =3rd coloumn'''
x=iris['data'][:,3:]  
y = (iris['target'] == 2).astype(np.int)
# print(y)
# print(x) 


# train a logistic regresion Classifier 
clf =LogisticRegression()
clf.fit(x,y)
example =clf.predict([[2.6]])
print(example)
#using matplotlib_to plot vizualization
x_new = np.linspace(0,3,100).reshape(-1,1)
y_prob =clf.predict_proba(x_new)
plt.plot(x_new,y_prob[:,1],"g-",label= "veginica")
plt.show()
print(x_new)




