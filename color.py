def Farberkennung(Kamera, MinWinkel, MaxWinkel, MinSaettigung, MaxSaettigung, MinHelligkeit, MaxHelligkeit):
    import cv2 as cv
    import numpy as np
    import datetime as dt

    cam = cv.VideoCapture(Kamera)       # Aufruf der Kamera
    # cam.set(cv.CAP_PROP_BUFFERSIZE, 1)  # Verarbeitungszeit maximal 1ms

    referencetime = dt.datetime.now()

    while True:  # While-Schleife, damit das Programm per Knopfdruck geschlossen werden kann

        if cv.waitKey(1) == ord("1"):   # Beim Drücken der Taste "1" wird
            print("Versuchsstart")      # in der Konsole der Text ausgegeben (zur Auswertung)

        _, img = cam.read()             # Auslesen der Kamera
        img = img[200:250, 100:500]     # Zuschneiden des Bildes

        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)  # Konvertierung in HSV-Farbraum

        # Farbton, Sättigung, Helligkeit
        untergrenze = np.array([MinWinkel, MinSaettigung, MinHelligkeit])       # Übernahme der Untergrenzen
        obergrenze = np.array([MaxWinkel, MaxSaettigung, MaxHelligkeit])        # Übernahme der Obergrenzen

        maske = cv.inRange(hsv, untergrenze, obergrenze)        # Zusammensetzung der Maskenbedingungen
        kombi = cv.bitwise_and(img, img, mask=maske)            # Anwenden der Maske auf farbiges Bild

        points = np.argwhere(maske > 0)  # Auslesen der Punkte, die sich von 0/schwarz unterschieden

        center, radius = cv.minEnclosingCircle(points)  # Kreiszeichnung um die gefilterten Pixel
        cv.circle(img, (int(center[1]), int(center[0])), int(radius), (255, 0, 0), 2)   # Zeichnen des Kreises
        cv.circle(img, (int(center[1]), int(center[0])), 1, (0, 0, 0), 2)               # Zeichnen des Zentrums

        skala = (center[1] - 202) * (80 / 365)      # Umskalieren von Pixel in cm
        now = dt.datetime.now()                     # Bestimmung der aktuellen Zeit
        delta = now - referencetime                 # Umrechnung in vergangene Zeit seit Start
        print(str(delta).replace('0:00:', '').replace('.', ','), str(skala).replace('.', ','))  # Konsolenausgabe

        cv.imshow('Farberkennung', img)         # Anzeigen des Bildes auf Monitor, zur Überwachung
        cv.imshow('HSV-Farbskala', hsv)         # Anzeige des Bildes im HSV-Farbraum
        cv.imshow('Maske', maske)               # Anzeigen der Maske
        cv.imshow('Angewandte Maske', kombi)    # Anzeigen des zusammengesetzten Bildes

        if cv.waitKey(1) == ord("0"):           # Abbruchbedingung der Schleife festgelegt als Knopfdruck 0
            break

    cam.release()                               # Freigeben der Kamera für andere Zwecke
    cv.destroyAllWindows()                      # Schließen aller Fenster, die durch Anwendung geöffnet wurden.
