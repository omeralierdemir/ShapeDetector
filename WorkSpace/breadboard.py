import numpy as np
import cv2
from matplotlib import pyplot as plt
import imutils
np.random.seed(0)  # seed for reproducibility

img = cv2.imread("../Images/kare.png")

x1 = np.random.randint(10, size=6)  # One-dimensional array
x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
x3 = np.random.randint(10, size=(4, 4, 5))  # Three-dimensional array

dizi = np.array([])

kume3 = set(())
print(type(dizi))
sets = {1,1,1,2,3,4,5,"omer"}
kume = set((1,2,3,4))
kume2 = set(((1,2),(3,4),(5,6)))
dizia = [1,2]
sets.add((dizia[0],dizia[1]))

dizi3 =  list(kume2)
dizia.remove(2)
print("sda",dizia)

#print(dizi3[0] == kume2 )
print((1,1) == [1,1])
kume3.add(1)
print(sets,len(sets),type(sets))
print(kume2.discard((1,2)),kume2, kume3,type(kume3))
resized = imutils.resize(img, width=300)

resized[100][80] = (255,0,0)

plt.imshow(resized)
plt.show()

di = [1,2,3,5]
di2 = [1,2,3,5]

di = [[1,2],[3,5]]
di2 = [[1,2],[3,5]]

if di == di2:
    print("omer")


print(di == di2)