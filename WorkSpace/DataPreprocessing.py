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

def findContourWithAprrox(image):
    cnts, ratio = findContour(image)
    koseSayisi = []

    for i in cnts:
        peri = cv2.arcLength(i, True)
        approx = cv2.approxPolyDP(i, 0.1 * peri, True)
        koseSayisi.append(approx)


def perimeterRadiusRelation(image):
    cnts, ratio = findContour(image)
    resized = imutils.resize(image, width=300)
    oranlar = []

    for i in cnts:
        perimeter = cv2.arcLength(i, True)
        (x, y), radius = cv2.minEnclosingCircle(i)
        center = (int(x), int(y))
        radius = int(radius) *2
        oran = round(perimeter / radius ,2)
        oranlar.append(oran)

        img = cv2.circle(resized, center, int(radius), (0, 255, 0), 2)
        cv2.imshow("Image", resized)
        cv2.waitKey(0)
#burada yapilan islem, tespit edilen seklin cevre uzunlugunu seklin üzerine cizilebilinen minumum alana sahip cemberin cabına oranı
# sistemimiz için bagımsız degisken olarak kullanılacaktır.

def findContourNumber(image):

    cnts,ratio = findContour(image)
    resized = imutils.resize(image, width=300)
    koseSayisi = []
    a = 0
    for i in cnts:
        cv2.drawContours(resized, [i], -1, (0, 255, 0), 2)

        peri = cv2.arcLength(i, True)
        approx = cv2.approxPolyDP(i, 0.1 * peri, True)# 0.1 değeri artırıldıpında yanlıs anlamadıysam diger noktalara olan maksimum degerde
                                                      #artıyor. Bu sebeple cikan kose noktalarinin sayisinda azalma oluyor. En cok azalma
                                                      # cemberler icin oluyor.
        koseSayisi.append(approx)
        print(peri,approx)
        print(len(koseSayisi[a]))
        a = a + 1
        cv2.imshow("Image", resized)
        cv2.waitKey(0)
       # print(len(cnts)) #sonradan ön işleme için bunu bir listede tutabilirsin.



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
# noktanın farkı ile karşılaştırılmasına dayanır. Eğer çıkan sonuc büyük ise muhtemel bir köşe çizilinebilir denmektedir. daha dogrusu
#muhtemel köse noktalarının sayısını köse olma olabiliritesi en yüksek olan degerlere indirgeme cabası.
# Bu veri KNN veya başka makine öğrenmesi algoritmalarında bağımsız değişken olarak kullanılacaktır.

