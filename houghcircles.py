def Kreiserkennung(Kamera, Aufloesung, Mindestabstand, Kantenwert, Rundheit, MinRadius, MaxRadius):
    import cv2 as cv
    import numpy as np
    import datetime as dt

    cam = cv.VideoCapture(Kamera)       # Aufruf der Kamera
    cam.set(cv.CAP_PROP_BUFFERSIZE, 1)  # Verarbeitungszeit maximal 1ms

    referencetime = dt.datetime.now()   # Bestimmung der Startzeit

    while True:  # While-Schleife, damit das Programm per Knopfdruck geschlossen werden kann

        if cv.waitKey(1) == ord("1"):   # Beim Drücken der Taste "1" wird
            print("Versuchsstart")      # in der Konsole der Text ausgegeben (zur Auswertung)

        _, img = cam.read()             # Auslesen der Kamera
        img = img[200:250, 100:500]     # Zuschneiden des Bildes

        cv.rectangle(img, (175, 0), (250, 3), (255, 255, 255), 10)
        cv.rectangle(img, (150, 34), (225, 50), (255, 255, 255), 10)
        cv.rectangle(img, (0, 0), (500, 40), (255, 255, 255), 10)

        grau = cv.cvtColor(img, cv.COLOR_BGR2GRAY)          # Konvertierung in Graustufen
        # blurr = cv.bilateralFilter(grau, 7, 60, 80)         # Verschwimmen des Bildes
        kanten = cv.Canny(grau, 30, 100)  # Ausgabe des Canny-Algs, ähnlich wie in HoughCircles

        # Anwendung der HoughCircles Funktion
        circles = cv.HoughCircles(grau, cv.HOUGH_GRADIENT,
                                  Aufloesung, Mindestabstand,
                                  param1=Kantenwert, param2=Rundheit,
                                  minRadius=MinRadius, maxRadius=MaxRadius)

        if circles is not None:
            circles = np.uint16(np.around(circles))     # Konvertieren der erkannten Kreise in U-Int
            for i in circles[0, :]:                     # Auslesen der Kreiszentren
                # Bild, Zentrum, Radius, Farbe in RGB, Dicke
                cv.circle(img, (i[0], i[1]), i[2], (255, 0, 0), 2)      # Zeichnen des Kreises
                cv.circle(img, (i[0], i[1]), 1, (0, 0, 0), 2)           # Zeichnen des Zentrums

                skala = (i[0] - 202) * (80 / 365)       # Umskalieren von Pixel in cm
                now = dt.datetime.now()                 # Bestimmung der aktuellen Zeit
                delta = now - referencetime             # Umrechnung in vergangene Zeit seit Start
                print(str(delta).replace('0:00:', '').replace('.', ','), str(skala).replace('.', ','))  # Ausgabe

        cv.imshow('Kreiserkennung', img)        # Anzeigen des Bildes auf Monitor, zur Überwachung
        # cv.imshow('Graustufen',     grau)       # Anzeigen des Graustufenbildes
        # cv.imshow('Bilateral',      blurr)      # Anzeigen des verschwommenen Bildes
        cv.imshow('Kantenaufnahme', kanten)     # Anzeigen des Kantenbildes

        if cv.waitKey(1) == ord("0"):           # Abbruchbedingung der Schleife festgelegt als Knopfdruck 0
            break

    cam.release()               # Freigeben der Kamera für andere Zwecke
    cv.destroyAllWindows()      # Schließen aller Fenster, die durch Anwendung geöffnet wurden.
