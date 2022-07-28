def Farberkennung(MinWinkel, MaxWinkel, MinSaettigung, MaxSaettigung, MinHelligkeit, MaxHelligkeit):

    import cv2 as cv
    import numpy as np

    cam = cv.VideoCapture(1)    # Auswahl der Kamera, wobei 0 --> Innenkamera und 1 --> Außenkamera

    while True:                 # While-Schleife, damit das Programm per Knopfdruck geschlossen werden kann

        _, img = cam.read()                                 # Auslesen der Kamera
        # img = img[100:200, 100:200]                       # Zuschneiden des Bildes

        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)            # Konvertierung in HSV-Farbraum

        # Farbton, Sättigung, Helligkeit
        untergrenze = np.array([MinWinkel, MinSaettigung, MinHelligkeit])   # Übernahme der Untergrenzen
        obergrenze = np.array([MaxWinkel, MaxSaettigung, MaxHelligkeit])    # Übernahme der Obergrenzen

        maske = cv.inRange(hsv, untergrenze, obergrenze)    # Zusammensetzung der Maskenbedingungen
        kombi = cv.bitwise_and(img, img, mask=maske)        # Anwenden der Maske auf farbiges Bild

        cv.imshow('Erkennungsabbild', img)      # Anzeigen des Bildes auf Monitor, zur Überwachung
        cv.imshow('HSV-Übertragung', hsv)       # Anzeige des Bildes im HSV-Farbraum
        cv.imshow('Maske', maske)               # Anzeigen der Maske
        cv.imshow('Angewandte Maske', kombi)    # Anzeigen des zusammengesetzten Bildes

        # Hier fehlt noch die Positionsausgabe

        if cv.waitKey(1) == ord("0"):       # Abbruchbedingung der Schleife festgelegt als Knopfdruck 0
            break

    cam.release()               # Freigeben der Kamera für andere Zwecke
    cv.destroyAllWindows()      # Schließen aller Fenster, die durch Anwendung geöffnet wurden.
