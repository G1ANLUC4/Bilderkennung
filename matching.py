def TemplateMatching(Kamera):

    import cv2 as cv

    # Öffnen des Vorlagebildes
    template = cv.imread('C:\\Users\\giann\\PycharmProjects\\Projektarbeit\\Fotos\\Ballfoto3.png', 0)

    b, h = template.shape[::-1]             # Speichern der Abmessungen der Vorlage
    b = round(b/2)                          # Halbieren der Breite der Vorlage
    h = round(h/2)                          # Halbieren der Höhe der Vorlage
    cv.imshow("Vorgabe", template)          # Anzeigen der Vorlage mittels der gesucht wird

    cam = cv.VideoCapture(Kamera)           # Aufruf der Kamera
    cam.set(cv.CAP_PROP_BUFFERSIZE, 1)      # Verarbeitungszeit maximal 1ms

    while True:                             # While-Schleife, damit das Programm per Knopfdruck geschlossen werden kann

        _, img = cam.read()                 # Auslesen der Kamera
        img = img[200:250, 100:500]         # Zuschneiden des Bildes

        grau = cv.cvtColor(img, cv.COLOR_BGR2GRAY)                          # Umwandlung in Graustufen

        erg = cv.matchTemplate(grau, template, cv.TM_CCORR_NORMED)          # Vergleichen von Video und Vorlage

        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(erg)              # Ausgabe der Extrema des Vergleichs
        cv.circle(img, (max_loc[0]+b, max_loc[1]+h), b, (255, 0, 0), 2)     # Zeichnen der Kreise um Maximum

        skala = (max_loc[0]-203)*(40/185)       # Umskalieren von Pixel in cm
        print(skala)                            # Ausgabe der x-Koordinate

        cv.imshow('Template Matching', img)     # Anzeigen des Bildes auf Monitor, zur Überwachung
        cv.imshow('Deckung', erg)               # Anzeigen des Überdeckungsabbildes
        cv.imshow('Grau', grau)                 # Anzeigen des Videoframes in Graustufen

        if cv.waitKey(1) == ord("0"):           # Abbruchbedingung der Schleife festgelegt als Knopfdruck 0
            break

    cam.release()               # Freigeben der Kamera für andere Zwecke
    cv.destroyAllWindows()      # Schließen aller Fenster, die durch Anwendung geöffnet wurden.
