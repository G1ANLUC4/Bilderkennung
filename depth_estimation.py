def Tiefenerkennung(Kamera, Aufloesung, Mindestabstand, Kantenwert, Rundheit, MinRadius, MaxRadius):

    import numpy as np
    import cv2 as cv

    # Auswahl des KI-Modells
    model = cv.dnn.readNet('C:\\Users\\giann\\PycharmProjects\\Projektarbeit\\models\\model-small.onnx')

    cam = cv.VideoCapture(Kamera)           # Aufruf der Kamera
    # cam.set(cv.CAP_PROP_BUFFERSIZE, 1)    # Verarbeitungszeit maximal 1ms

    while True:                             # While-Schleife, damit das Programm per Knopfdruck geschlossen werden kann

        _, img = cam.read()                 # Auslesen der Kamera
        img = img[200:250, 100:500]         # Zuschneiden des Bildes
        hoehe, breite, farbe = img.shape    # Auslesen der Maße für später

        # Erstellen des blobs für KI
        blob = cv.dnn.blobFromImage(img, 1 / 255., (256, 256),
                                    (123.675, 116.28, 103.53),
                                    True, False)

        model.setInput(blob)                # Anwenden des blobs auf KI
        output = model.forward()            # Ausgabe der KI

        output = output[0, :, :]                            # Zwischenspeichern des Ausgabe-Arrays
        output = cv.resize(output, (breite, hoehe))         # Anpassen des Ausgabebildes in Ursprungsform

        # Normalisierung in andere Farbräume
        outfordm = cv.normalize(output, None, 0, 1, norm_type=cv.NORM_MINMAX, dtype=cv.CV_32F)
        output = cv.normalize(outfordm, None, 0, 255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8U)
        outfordmht = cv.cvtColor(img, cv.COLOR_BGR2HSV)

        # Erkennen von Kreisen in der Heatmap
        circles = cv.HoughCircles(output, cv.HOUGH_GRADIENT,
                                  Aufloesung, Mindestabstand,
                                  param1=Kantenwert, param2=Rundheit,
                                  minRadius=MinRadius, maxRadius=MaxRadius)

        if circles is not None:
            circles = np.uint16(np.around(circles))                 # Konvertieren der Erkannten kreise in U-Int
            for i in circles[0, :]:                                 # Auslesen der Kreiszentren
                # Bild, Zentrum, Radius, Farbe in RGB, Dicke
                cv.circle(img, (i[0], i[1]), i[2], (255, 0, 0), 5)  # Zeichnen des Kreises
                cv.circle(img, (i[0], i[1]), 1, (0, 0, 0), 5)       # Zeichnen des Zentrums

                skala = (i[0]-203)*(40/185)         # Umskalieren von Pixel in cm
                print(skala)                        # Ausgabe der Position in Konsole

        cv.imshow('Tiefenerkennung', img)           # Anzeigen des Bildes auf Monitor, zur Überwachung
        cv.imshow('Depth Map', outfordm)            # Anzeigen der Depth Map
        cv.imshow('Depth Map Heat', outfordmht)     # Anzeigen der Depth Map im Heat Map Stil

        if cv.waitKey(1) == ord("0"):               # Abbruchbedingung der Schleife festgelegt als Knopfdruck 0
            break

    cam.release()           # Freigeben der Kamera für andere Zwecke
    cv.destroyAllWindows()  # Schließen aller Fenster, die durch Anwendung geöffnet wurden.
