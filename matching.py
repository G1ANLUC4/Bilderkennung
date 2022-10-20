def TemplateMatching(Kamera):
    import cv2 as cv
    import datetime as dt

    # Öffnen des Vorlagebildes
    template = cv.imread('C:\\Users\\giann\\PycharmProjects\\Projektarbeit\\Fotos\\Ballfoto3.png', 0)

    b, h = template.shape[::-1]  # Speichern der Abmessungen der Vorlage
    b = round(b / 2)  # Halbieren der Breite der Vorlage
    h = round(h / 2)  # Halbieren der Höhe der Vorlage
    cv.imshow("Vorgabe", template)  # Anzeigen der Vorlage mittels der gesucht wird

    cam = cv.VideoCapture(Kamera)  # Aufruf der Kamera
    # cam.set(cv.CAP_PROP_BUFFERSIZE, 1)      # Verarbeitungszeit maximal 1ms
    referencetime = dt.datetime.now()

    while True:  # While-Schleife, damit das Programm per Knopfdruck geschlossen werden kann

        if cv.waitKey(1) == ord("1"):  # Beim Drücken der Taste "1" wird
            print("Versuchsstart")  # in der Konsole der Text ausgegeben (zur Auswertung)

        _, img = cam.read()  # Auslesen der Kamera
        img = img[207:237, 110:490]  # Zuschneiden des Bildes

        mean = img.mean(axis=0).mean(axis=0)  # Bestimmung der mittleren Bildfarbe
        cv.rectangle(img, (0, 0), (390, 3), (mean[0], mean[1], mean[2]), 7)  # Umrandung des Bildes im Bildfarbe,
        cv.rectangle(img, (0, 25), (390, 30), (mean[0], mean[1], mean[2]),
                     7)  # damit ein kleinerer Ausschnitt ausgewertet werden kann

        grau = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # Umwandlung in Graustufen

        erg = cv.matchTemplate(grau, template, cv.TM_CCORR_NORMED)  # Vergleichen von Video und Vorlage

        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(erg)  # Ausgabe der Extrema des Vergleichs
        cv.circle(img, (min_loc[0] + b, min_loc[1] + h), b, (255, 0, 0), 2)  # Zeichnen der Kreise um Maximum

        skala = ((min_loc[0] - 190) * (80 / 380))  # Umskalieren von Pixel in cm

        now = dt.datetime.now()  # Bestimmung der aktuellen Zeit
        delta = now - referencetime  # Umrechnung in vergangene Zeit seit Start
        print(str(delta).replace('0:00:', '').replace('.', ','), str(skala).replace('.', ','))  # Ausgabe

        cv.imshow('Template Matching', img)  # Anzeigen des Bildes auf Monitor, zur Überwachung
        cv.imshow('Deckung', erg)  # Anzeigen des Überdeckungsabbildes
        cv.imshow('Grau', grau)  # Anzeigen des Videoframes in Graustufen

        if cv.waitKey(1) == ord("0"):  # Abbruchbedingung der Schleife festgelegt als Knopfdruck 0
            break

    cam.release()  # Freigeben der Kamera für andere Zwecke
    cv.destroyAllWindows()  # Schließen aller Fenster, die durch Anwendung geöffnet wurden.
