def Kreiserkennung(Aufloesung, Mindestabstand, Kantenwert, Rundheit, MinRadius, MaxRadius):

    import cv2 as cv
    import numpy as np

    template = cv.imread('Fotos/Testbild.png', 0)   # Öffnen des Vorlagebildes
    cv.imshow("Vorgabe", template)                  # Anzeigen der Vorlage

    while True:                 # While-Schleife, damit das Programm per Knopfdruck geschlossen werden kann

        grau = cv.cvtColor(template, cv.COLOR_BGR2GRAY)     # Konvertierung in Graustufen
        kanten = cv.Canny(grau, 30, 100)                    # Ausgabe des Canny-Algs, ähnlich wie in HoughCircles

        circles = cv.HoughCircles(grau, cv.HOUGH_GRADIENT,                     # Anwendung der HoughCircles Funktion
                                  Aufloesung, Mindestabstand,
                                  param1=Kantenwert, param2=Rundheit,
                                  minRadius=MinRadius, maxRadius=MaxRadius)

        if circles is not None:
            circles = np.uint16(np.around(circles))                     # Konvertieren der erkannten Kreise in U-Int
            for i in circles[0, :]:                                     # Auslesen der Kreiszentren
                # Bild, Zentrum, Radius, Farbe in RGB, Dicke
                cv.circle(template, (i[0], i[1]), i[2], (255, 0, 0), 5)      # Zeichnen des Kreises
                cv.circle(template, (i[0], i[1]), 1, (0, 0, 0), 5)           # Zeichnen des Zentrums
                print(i[0], i[1])                                       # Ausgabe der x und y Koordinate

        cv.imshow('Kreiserkennung', template)        # Anzeigen des Bildes auf Monitor, zur Überwachung
        cv.imshow('Graustufen', grau)           # Anzeigen des Graustufenbildes
        cv.imshow('Kantenerkennung', kanten)    # Anzeigen des Kantenbildes

        if cv.waitKey(1) == ord("0"):           # Abbruchbedingung der Schleife festgelegt als Knopfdruck 0
            break

    cv.destroyAllWindows()      # Schließen aller Fenster, die durch Anwendung geöffnet wurden.
