# loading required modules 
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier  #its  a classifier
iris = datasets.load_iris()  # load iris data set 
#loading_dataset
# print(iris.DESCR)
# to describe
features = iris.data
label = iris.target
print(features[0],label[0])   


# training the classifier 
clf = KNeighborsClassifier   
clf.fit(features,label)

preds =clf.predict([[1,1,1,1]])  #predict the elemnt that has be input [[1,1,1,1]]
print(preds)