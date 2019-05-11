import cv2
import imutils
from WorkSpace import DataPreprocessing
from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
#from sklearn.metrics import confusion_matrix
import sklearn.metrics
from sklearn.preprocessing import LabelEncoder
import pandas as pd

"""
le = LabelEncoder()
a = sklearn.metrics

veriler = pd.read_csv("../Veriler/veriler.csv")

x_train = veriler.iloc[:,0:3].values
y_train = veriler.iloc[:,3].values
y_train = le.fit_transform(y_train)

print(x_train,y_train)

knn = KNeighborsClassifier(n_neighbors=3,metric="minkowski")
X_train, x_test, Y_train, y_test = train_test_split(x_train,y_train,random_state=0,test_size=0.33)
knn.fit(x_train,y_train)
y_pred = knn.predict(x_test)

cnn = a.confusion_matrix(y_test,y_pred)
sonuc = a.accuracy_score(y_pred,y_test)


print(cnn)
print(sonuc)
print(knn.score(x_test,y_test))

"""

image cv2.imread()







