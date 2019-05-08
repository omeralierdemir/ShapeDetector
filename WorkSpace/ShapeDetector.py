import cv2
import imutils
from WorkSpace import DataPreprocessing
from matplotlib import pyplot as plt




dt = DataPreprocessing
image = cv2.imread("../Images/kare.png")

#dt.cizdir(image)
a = dt.perimeterRadiusRelation(image)
b = dt.findContourNumber(image)
c = dt.findLocicalEdge(image)


resized = imutils.resize(image, width=300)

# for söngüsü dönder ekeman sayısı kadar. zaten ratio haric geri kalanın length i tutulacak.
ratio = image.shape[0] / float(resized.shape[0])

# convert the resized image to grayscale, blur it slightly,
# and threshold it
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
print(gray.shape[0],gray.shape[1])
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

# find contours in the thresholded image and initialize the
# shape detector
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

""" 
image[100,80] = (0,0,255)
plt.imshow(image)
plt.show()
"""






