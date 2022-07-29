def Farberkennung(MinWinkel, MaxWinkel, MinSaettigung, MaxSaettigung, MinHelligkeit, MaxHelligkeit):

    import cv2 as cv
    import numpy as np

    cam = cv.VideoCapture(1)            # Auswahl der Kamera, wobei 0 --> Innenkamera und 1 --> Außenkamera
    cam.set(cv.CAP_PROP_BUFFERSIZE, 1)  # Verarbeitungszeit maximal 1ms

    while True:                 # While-Schleife, damit das Programm per Knopfdruck geschlossen werden kann

        _, img = cam.read()                                 # Auslesen der Kamera
        # img = img[100:200, 100:200]                       # Zuschneiden des Bildes

        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)            # Konvertierung in HSV-Farbraum

        # Farbton, Sättigung, Helligkeit
        untergrenze = np.array([MinWinkel, MinSaettigung, MinHelligkeit])   # Übernahme der Untergrenzen
        obergrenze = np.array([MaxWinkel, MaxSaettigung, MaxHelligkeit])    # Übernahme der Obergrenzen

        maske = cv.inRange(hsv, untergrenze, obergrenze)    # Zusammensetzung der Maskenbedingungen
        kombi = cv.bitwise_and(img, img, mask=maske)        # Anwenden der Maske auf farbiges Bild

        points = np.argwhere(maske > 0)                     # Auslesen der
        center, radius = cv.minEnclosingCircle(points)
        cv.circle(img, (int(center[1]), int(center[0])), int(radius), (255, 0, 0), 5)   # Zeichnen des Kreises
        cv.circle(img, (int(center[1]), int(center[0])), 1, (0, 0, 0), 5)               # Zeichnen des Zentrums
        print(int(center[1]), int(center[0]))                                           # Ausgabe der x und y Koordinate

        cv.imshow('Farberkennung', img)           # Anzeigen des Bildes auf Monitor, zur Überwachung
        # cv.imshow('HSV-Farbskala', hsv)         # Anzeige des Bildes im HSV-Farbraum
        # cv.imshow('Maske', maske)               # Anzeigen der Maske
        # cv.imshow('Angewandte Maske', kombi)    # Anzeigen des zusammengesetzten Bildes

        if cv.waitKey(1) == ord("0"):       # Abbruchbedingung der Schleife festgelegt als Knopfdruck 0
            break

    cam.release()               # Freigeben der Kamera für andere Zwecke
    cv.destroyAllWindows()      # Schließen aller Fenster, die durch Anwendung geöffnet wurden.
