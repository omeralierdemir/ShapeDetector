import cv2
import imutils
from WorkSpace import DataPreprocessing
import pandas as pd
from matplotlib import pyplot as plt



dt = DataPreprocessing
image = cv2.imread("../Images/altigen.png")
contourEdgeNumbers = []
contourNumbers = []
shapeClass = []
#dt.cizdir(image)
ratio = dt.perimeterRadiusRelation(image)
contour = dt.findContourNumber(image)
contourEdge = dt.findLocicalEdge(image)

df = pd.read_csv("../Veriler/veriler.csv",index_col=False)
#print(df)
#df = pd.DataFrame()
print(type(df))

for i in range(len(ratio)):

    contourEdgeNumbers.append(len(contourEdge[i]))
    contourNumbers.append(len(contour[i]))
    shapeClass.append("altigen")

df2 = pd.DataFrame({"ratio":ratio,
                    "contourApprox":contourNumbers,
                    "contourEdge":contourEdgeNumbers,
                    "shapeClass":shapeClass})

print("sdas",df2)
df = df.append(df2,sort=False,ignore_index=True)
df.to_csv("../Veriler/veriler.csv",index = False)

# bu değerleri csv formatıyla tutup her yenilemede üzerine yazmalısın
print(df)