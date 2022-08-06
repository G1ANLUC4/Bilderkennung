def TemplateMatching(Kamera, Aufloesung):

    import cv2 as cv
    import numpy as np

    template = cv.imread('Fotos/Ballfoto3.png', 0)      # Öffnen des Vorlagebildes
    cv.imshow("Vorgabe", template)                      # Anzeigen der Vorlage mittels der gesucht wird

    cam = cv.VideoCapture(Kamera)           # Aufruf der Kamera
    # cam.set(cv.CAP_PROP_BUFFERSIZE, 1)    # Verarbeitungszeit maximal 1ms

    while True:                 # While-Schleife, damit das Programm per Knopfdruck geschlossen werden kann

        _, img = cam.read()                                 # Auslesen der Kamera
        # img = img[100:200, 100:200]                       # Zuschneiden des Bildes

        grau = cv.cvtColor(img, cv.COLOR_BGR2GRAY)          # Umwandlung in Graustufen

        erg = cv.matchTemplate(grau, template, cv.TM_CCORR_NORMED)      # Vergleichen von Video und Vorlage
        points = np.argwhere(erg <= Aufloesung)                         # Auswahl der Punkte mit großer Übereinstimmung

        center, radius = cv.minEnclosingCircle(points)                  # Kreiszeichnung um die gefilterten Pixel
        cv.circle(img, (int(center[1]), int(center[0])), int(radius), (255, 0, 0), 5)   # Zeichnen des Kreises
        cv.circle(img, (int(center[1]), int(center[0])), 1, (0, 0, 0), 5)               # Zeichnen des Zentrums
        print(int(center[1]), int(center[0]))                                           # Ausgabe der x und y Koordinate

        cv.imshow('Template Matching', img)     # Anzeigen des Bildes auf Monitor, zur Überwachung
        cv.imshow('Deckung', erg)               # Anzeigen des Überdeckungsabbildes
        cv.imshow('Grau', grau)                 # Anzeigen des Videoframes in Graustufen

        if cv.waitKey(1) == ord("0"):           # Abbruchbedingung der Schleife festgelegt als Knopfdruck 0
            break

    cam.release()               # Freigeben der Kamera für andere Zwecke
    cv.destroyAllWindows()      # Schließen aller Fenster, die durch Anwendung geöffnet wurden.


