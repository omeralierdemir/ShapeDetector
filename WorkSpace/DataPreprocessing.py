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
    resized = imutils.resize(image, width=300)

    for i in cnts:
        cv2.drawContours(resized, [i], -1, (0, 255, 0), 2)
        cv2.imshow("Image", resized)
        cv2.waitKey(0)
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
            if (j[0][0],j[0][1]) not in karaKume:
                for k in i:# cnts de sıkıntı var
                    b = list(k[0])

                    if abs(k[0][0] - j[0][0]) < abs(cX - j[0][0]) and abs(k[0][1] - j[0][1]) < abs(cY - j[0][1]):
                        if a != b:
                            karaKume.add((k[0][0],k[0][1]))
                    else:

                        beyazKume.add((k[0][0],k[0][1])) #tuple şeklinde ekledik çünkü set veri yapısı list türünde eleman almıyor, çünkü list değişkendir

                        # hacı bak burada karalistedeki elemanlarıda beyaz listeye ekliyo ama sen zaten en sonunda kara listedeki elemanları
                        # beyaz listeden temizleyeceğin için ayrı bir if değimi eklenmemiştir.

        beyazListe = list(beyazKume)
        karaListe = list(karaKume)


        for point in karaListe:

            if point in beyazListe:

                beyazListe.remove(point)


        koseSayisi.append(beyazListe)

        beyazKume.clear()
        karaKume.clear()


# burada işeyen kodun mantığı findContour() ile bulunan bir köşe noktasından diğer bulunan köşe noktalarına kaç adet köşe
# çizilebileceğimizi test etmeye çalışmaktadır. Algoritmanın işleyişi:
# > kıyaslanan noktaların birbirinden farkını alarak (x-y eksenleri için ayrı ayrı) çıkan sonucu şeklin orta noktası ile kıyaslanan
# noktanın farkı ile karşılaştırılmasına dayanır. Eğer çıkan sonuc büyük ise muhtemel bir köşe çizilinebilir denmektedir.
# Bu veri KNN veya başka makine öğrenmesi algoritmalarında bağımsız değişken olarak kullanılacaktır.

