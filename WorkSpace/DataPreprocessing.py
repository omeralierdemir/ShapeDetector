import cv2
import imutils
import numpy as np
from matplotlib import pyplot as plt



def findContour(image):
    resized = imutils.resize(image, width=300)
    ratio = image.shape[0] / float(resized.shape[0])


    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]


    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    return cnts,ratio
def findContourNumber(image):

    cnts,ratio = findContour(image)

    for i in cnts:

        print(len(cnts)) #sonradan ön işleme için bunu bir listede tutabilirsin.

def findLocicalEdge(image):

    koseSayisi = []
    karaListe = []
    beyazKume = set(()) # used set data struct for non dublicate value
    karaKume = set(())
    cnts,ratio = findContour(image)

    for i in cnts:
        M = cv2.moments(i)
        cX = int((M["m10"] / M["m00"]))
        cY = int((M["m01"] / M["m00"]))
        for j in i:
            a = list(j[0])
            if j not in karaListe:
                for k in cnts[0]:
                    b = list(k[0])

                    if abs(k[0][0] - j[0][0]) < abs(cY - j[0][0]) and abs(k[0][1] - j[0][1]) < abs(cX - j[0][1]):
                        if a != b:
                            karaListe.append([k[0][0],k[0][0]])
                    else:

                        beyazKume.add((k[0][0],k[0][1])) #tuple şeklinde ekledik çünkü set veri yapısı list türünde eleman almıyor, çünkü list değişkendir

                        # hacı bak burada karalistedeki elemanlarıda beyaz listeye ekliyo ama sen zaten en sonunda kara listedeki elemanları
                        # beyaz listeden temizleyeceğin için ayrı bir if değimi eklenmemiştir.

            beyazListe = list(beyazKume)

            #for da index index karşılaştırma yapcan biri tuple biri liste
            for point in karaListe:

                if (point[0],point[1]) in beyazListe:

                    beyazListe.remove((point[0],point[1]))


            koseSayisi.append(beyazListe)

            beyazKume.clear()
            karaListe.clear()



#başkan for j in karalist i kontrol et
# for döngüsü yanlış sayıda dönüyo debugla hatayı tespit et
# karalistedede dublicate eleman var onu çöz
