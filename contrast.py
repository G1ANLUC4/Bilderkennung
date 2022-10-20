def Kontrasterkennung(Kamera, Untergrenze, Obergrenze, Ordnung, Iterationen, MinFlaeche, MaxFlaeche):
    import cv2 as cv
    import numpy as np
    import datetime as dt

    abstand = 16
    xval = 0
    yval = 0
    rval = 0
    x = 0

    cam = cv.VideoCapture(Kamera)       # Aufruf der Kamera
    # cam.set(cv.CAP_PROP_BUFFERSIZE, 1)  # Verarbeitungszeit maximal 1ms

    referencetime = dt.datetime.now()   # Bestimmung der Startzeit

    while True:  # While-Schleife, damit das Programm per Knopfdruck geschlossen werden kann

        if cv.waitKey(1) == ord("1"):   # Beim Drücken der Taste "1" wird
            print("Versuchsstart")      # in der Konsole der Text ausgegeben (zur Auswertung)

        _, img = cam.read()             # Auslesen der Kamera
        img = img[207:237, 110:490]     # Zuschneiden des Bildes

        src_img = img.astype(np.uint8)                  # Umformatieren des Bildes für OTSU-Threshold
        grau = cv.cvtColor(src_img, cv.COLOR_BGR2GRAY)  # Umwandeln in Graustufen
        verschwommen = cv.medianBlur(grau, 3)           # Entschärfen des Bildes

        # Threshold-Analyse teilt Bild in schwarz/weiß bzw. 1/0 auf.
        thresh = cv.threshold(verschwommen, Untergrenze, Obergrenze, cv.THRESH_BINARY_INV)[1]

        struktur = cv.getStructuringElement(cv.MORPH_ELLIPSE, (Ordnung, Ordnung))               # Erstellen der Maske
        ergebnis = cv.morphologyEx(thresh, cv.MORPH_OPEN, struktur, iterations=Iterationen)     # Durchsuchen mit Maske

        # Herausziehen aller Konturen auf geraden Linien
        kontur = cv.findContours(ergebnis, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

        if len(kontur) == 2:        # Fallunterscheidung für verschiedene Konturanzahlen
            kontur = kontur[0]
        else:
            kontur = kontur[1]

        for c in kontur:
            area = cv.contourArea(c)                    # Auslesen der Konturflächen

            if MinFlaeche < area < MaxFlaeche:          # Filtern der Konturen nach Fläche
                ((x, y), r) = cv.minEnclosingCircle(c)  # Umkreisen der Konturen mit Kreisparametern

                if abs(15 - y) < abstand:   # Iterative Sortierung der Konturen, die mittiger liegen (y-Achse)
                    abstand = 15 - y        # Wenn die kontur mittiger lieg, wird ein neuer Abstand definiert
                    xval = int(x)           # Speicherung der Parameter des mittigen Kreises
                    yval = int(y)
                    rval = int(r)

        cv.circle(img, (int(xval), int(yval)), int(rval), (255, 0, 0), 2)   # Zeichnen des Kreises
        cv.circle(img, (int(xval), int(yval)), 1, (0, 0, 0), 2)             # Zeichnen des Zentrums

        skala = (int(x) - 290) * (80 / 380)     # Umskalieren von Pixel in cm

        now = dt.datetime.now()                 # Bestimmen der aktuellen Zeit
        delta = now - referencetime             # Umrechnung in vergangene Zeit seit Start
        print(str(delta).replace('0:00:', '').replace('.', ','), str(skala).replace('.', ','))  # Ausgabe

        cv.imshow('Kontrastsuche', img)             # Anzeigen des Bildes auf Monitor, zur Überwachung
        # cv.imshow('circles detected', grau)       # Anzeigen des Graustufenbildes
        # cv.imshow('verschwommen', verschwommen)   # Anzeigen des verschwommenen Bildes
        # cv.imshow('Thresh-Analyse', thresh)       # Anzeigen des Analyse-Ergebnisses
        cv.imshow('opening', ergebnis)              # Anzeigen nach Durchlauf der Bit-Maske

        if cv.waitKey(1) == ord("0"):   # Abbruchbedingung der Schleife festgelegt als Knopfdruck 0
            break

    cam.release()                       # Freigeben der Kamera für andere Zwecke
    cv.destroyAllWindows()              # Schließen aller Fenster, die durch Anwendung geöffnet wurden.
