def Kreiserkennung(Kamera, Aufloesung, Mindestabstand, Kantenwert, Rundheit, MinRadius, MaxRadius):

    import cv2 as cv
    import numpy as np

    cam = cv.VideoCapture(Kamera)           # Aufruf der Kamera
    cam.set(cv.CAP_PROP_BUFFERSIZE, 1)      # Verarbeitungszeit maximal 1ms

    while True:                 # While-Schleife, damit das Programm per Knopfdruck geschlossen werden kann

        _, img = cam.read()                                 # Auslesen der Kamera
        # img = img[100:200, 100:200]                       # Zuschneiden des Bildes

        grau = cv.cvtColor(img, cv.COLOR_BGR2GRAY)          # Konvertierung in Graustufen
        blurr = cv.bilateralFilter(grau, 10, 50, 50)        # Verschwimmen des Bildes
        kanten = cv.Canny(grau, 30, 100)                    # Ausgabe des Canny-Algs, ähnlich wie in HoughCircles

        circles = cv.HoughCircles(blurr, cv.HOUGH_GRADIENT,                     # Anwendung der HoughCircles Funktion
                                  Aufloesung, Mindestabstand,
                                  param1=Kantenwert, param2=Rundheit,
                                  minRadius=MinRadius, maxRadius=MaxRadius)

        if circles is not None:
            circles = np.uint16(np.around(circles))                     # Konvertieren der erkannten Kreise in U-Int
            for i in circles[0, :]:                                     # Auslesen der Kreiszentren
                # Bild, Zentrum, Radius, Farbe in RGB, Dicke
                cv.circle(img, (i[0], i[1]), i[2], (255, 0, 0), 5)      # Zeichnen des Kreises
                cv.circle(img, (i[0], i[1]), 1, (0, 0, 0), 5)           # Zeichnen des Zentrums
                print(i[0], i[1])                                       # Ausgabe der x und y Koordinate

        cv.imshow('Kreiserkennung', img)        # Anzeigen des Bildes auf Monitor, zur Überwachung
        cv.imshow('Graustufen', grau)           # Anzeigen des Graustufenbildes
        cv.imshow('Bilateral', blurr)           # Anzeigen des verschwommenen Bildes
        cv.imshow('Kantenerkennung', kanten)    # Anzeigen des Kantenbildes

        if cv.waitKey(1) == ord("0"):           # Abbruchbedingung der Schleife festgelegt als Knopfdruck 0
            break

    cam.release()               # Freigeben der Kamera für andere Zwecke
    cv.destroyAllWindows()      # Schließen aller Fenster, die durch Anwendung geöffnet wurden.
