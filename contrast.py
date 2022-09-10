def Kontrasterkennung(Kamera, Untergrenze, Obergrenze, Ordnung, Iterationen, MinFlaeche, MaxFlaeche):

    import cv2 as cv
    import numpy as np

    cam = cv.VideoCapture(Kamera)       # Aufruf der Kamera
    cam.set(cv.CAP_PROP_BUFFERSIZE, 1)  # Verarbeitungszeit maximal 1ms

    while True:                         # While-Schleife, damit das Programm per Knopfdruck geschlossen werden kann

        _, img = cam.read()                                 # Auslesen der Kamera
        img = img[200:250, 100:500]                         # Zuschneiden des Bildes

        src_img = img.astype(np.uint8)                      # Umformatieren des Bildes für OTSU-Threshold
        grau = cv.cvtColor(src_img, cv.COLOR_BGR2GRAY)      # Umwandeln in Graustufen
        verschwommen = cv.medianBlur(grau, 3)               # Entschärfen des Bildes

        # Threshold-Analyse teilt Bild in schwarz/weiß bzw. 1/0 auf.
        thresh = cv.threshold(verschwommen, Untergrenze, Obergrenze,
                              cv.THRESH_BINARY + cv.THRESH_OTSU + cv.THRESH_BINARY_INV)[1]

        struktur = cv.getStructuringElement(cv.MORPH_ELLIPSE, (Ordnung, Ordnung))               # Erstellen der Maske
        ergebnis = cv.morphologyEx(thresh, cv.MORPH_OPEN, struktur, iterations=Iterationen)     # Durchsuchen mit Maske

        # Herausziehen aller Konturen auf geraden Linien
        kontur = cv.findContours(ergebnis, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

        if len(kontur) == 2:        # Unterscheidung der Konturlänge
            kontur = kontur[0]
        else:
            kontur = kontur[1]

        for c in kontur:
            peri = cv.arcLength(c, True)                        # Abweichen von erkannter Kontur zur Eingabe-Matrix
            approx = cv.approxPolyDP(c, 0.1 * peri, True)       # Genauigkeit der Kontur
            area = cv.contourArea(c)                            # Fläche der erkannten Kontur

            if len(approx) > 3 and MinFlaeche < area < MaxFlaeche:              # Beurteilung des Kreises
                ((x, y), r) = cv.minEnclosingCircle(c)
                cv.circle(img, (int(x), int(y)), int(r), (255, 0, 0), 2)        # Zeichnen des Kreises
                cv.circle(img, (int(x), int(y)), 1, (0, 0, 0), 2)               # Zeichnen des Zentrums

                skala = (int(x)-203)*(40/185)       # Umskalieren von Pixel in cm
                print(skala)                        # Ausgabe der x-Koordinate

        cv.imshow('Kontrastsuche', img)             # Anzeigen des Bildes auf Monitor, zur Überwachung
        cv.imshow('circles detected', grau)         # Anzeigen des Graustufenbildes
        cv.imshow('verschwommen', verschwommen)     # Anzeigen des verschwommenen Bildes
        cv.imshow('Thresh-Analyse', thresh)         # Anzeigen des Analyse-Ergebnisses
        cv.imshow('opening', ergebnis)              # Anzeigen nach Durchlauf der Bit-Maske

        if cv.waitKey(1) == ord("0"):               # Abbruchbedingung der Schleife festgelegt als Knopfdruck 0
            break

    cam.release()               # Freigeben der Kamera für andere Zwecke
    cv.destroyAllWindows()      # Schließen aller Fenster, die durch Anwendung geöffnet wurden.
