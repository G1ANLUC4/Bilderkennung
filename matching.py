def TemplateMatching(Aufloesung):

    import cv2 as cv
    import numpy as np

    template = cv.imread('Fotos/Ballfoto3.png', 0)
    cv.imshow("Vorgabe", template)

    cam = cv.VideoCapture(1)                # Auswahl der Kamera, wobei 0 --> Innenkamera und 1 --> Außenkamera
    # cam.set(cv.CAP_PROP_BUFFERSIZE, 1)    # Verarbeitungszeit maximal 1ms

    while True:                 # While-Schleife, damit das Programm per Knopfdruck geschlossen werden kann

        _, img = cam.read()                                 # Auslesen der Kamera
        # img = img[100:200, 100:200]                       # Zuschneiden des Bildes

        grau = cv.cvtColor(img, cv.COLOR_BGR2GRAY)          # Umwandlung in Graustufen

        erg = cv.matchTemplate(grau, template, cv.TM_CCORR_NORMED)
        points = np.argwhere(erg <= Aufloesung)

        center, radius = cv.minEnclosingCircle(points)
        cv.circle(img, (int(center[1]), int(center[0])), int(radius), (255, 0, 0), 5)  # Zeichnen des Kreises
        cv.circle(img, (int(center[1]), int(center[0])), 1, (0, 0, 0), 5)  # Zeichnen des Zentrums
        print(int(center[1]), int(center[0]))  # Ausgabe der x und y Koordinate

        cv.imshow('Deckung', erg)
        cv.imshow('Grau', grau)
        cv.imshow('Erkennungsbild', img)

        if cv.waitKey(1) == ord("0"):  # Abbruchbedingung der Schleife festgelegt als Knopfdruck 0
            break

    cam.release()               # Freigeben der Kamera für andere Zwecke
    cv.destroyAllWindows()      # Schließen aller Fenster, die durch Anwendung geöffnet wurden.


