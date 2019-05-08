import cv2
import imutils
from WorkSpace import DataPreprocessing
import pandas as pd
from matplotlib import pyplot as plt



dt = DataPreprocessing
image = cv2.imread("../Images/kare.png")
contourEdgeNumbers = []
contourNumbers = []
shapeClass = []
#dt.cizdir(image)
ratio = dt.perimeterRadiusRelation(image)
contour = dt.findContourNumber(image)
contourEdge = dt.findLocicalEdge(image)

df = pd.DataFrame()



for i in range(len(ratio)):

    contourEdgeNumbers.append(len(contourEdge[i]))
    contourNumbers.append(len(contour[i]))
    shapeClass.append("kare")

df2 = pd.DataFrame({"ratio":ratio,
                    "contourApprox":contourNumbers,
                    "contourEdge":contourEdgeNumbers,
                    "shapeClass":shapeClass})

df = df.append(df2,ignore_index = True)

# bu değerleri csv formatıyla tutup her yenilemede üzerine yazmalısın
print(df)