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

def sistemTest(veriler):
    le = LabelEncoder()
    a = sklearn.metrics



    x_train = veriler.iloc[:,0:3].values
    y_train = veriler.iloc[:,3].values
    y_train = le.fit_transform(y_train)



    knn = KNeighborsClassifier(n_neighbors=9,metric="minkowski")
    # euclidean : 0.9104477611940298, minkowski: 0.9104477611940298 manhattan:k=5 için  0.8656716417910447 k:3 için 0.9104477611940298


    X_train, x_test, Y_train, y_test = train_test_split(x_train,y_train,random_state=0,test_size=0.33)
    knn.fit(x_train,y_train)
    y_pred = knn.predict(x_test)

    cnn = a.confusion_matrix(y_test,y_pred)
    sonuc = a.accuracy_score(y_pred,y_test)


    print(cnn)
    print(sonuc)
    print(knn.score(x_test,y_test))


def uygulamaTest(image,veriler):

    contourEdgeNumbers = []
    contourNumbers = []
    shapeClass = []
    dt = DataPreprocessing


    cnts, shapeRatio = dt.findContour(image)


    ratio = dt.perimeterRadiusRelation(cnts)
    contour = dt.findContourNumber(image,cnts)
    contourEdge = dt.findLocicalEdge(image,cnts)

    for i in range(len(ratio)):

        contourEdgeNumbers.append(len(contourEdge[i]))
        contourNumbers.append(len(contour[i]))
        shapeClass.append("altigen")

    testDF = pd.DataFrame({"ratio":ratio,
                        "contourApprox":contourNumbers,
                        "contourEdge":contourEdgeNumbers})
    testData = testDF.iloc[:,0:3].values
    x_train = veriler.iloc[:,0:3].values
    y_train = veriler.iloc[:,3].values #label encoder yapmadın daha
    print(testData)


    knn = KNeighborsClassifier(n_neighbors=3,metric="minkowski") # euclidean


    knn.fit(x_train,y_train)
    y_pred = knn.predict(testData)
    print(y_pred)

    dt.cizdir(image,y_pred)





if __name__ == '__main__':
    image = cv2.imread("../Images/shapes_and_colors.png")
    veriler = pd.read_csv("../Veriler/veriler.csv")

    uygulamaTest(image,veriler)

   # sistemTest(veriler)