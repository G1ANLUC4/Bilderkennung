def Unbekannt():

    import cv2 as cv

    cam = cv.VideoCapture(1)                # Auswahl der Kamera, wobei 0 --> Innenkamera und 1 --> Außenkamera
    # cam.set(cv.CAP_PROP_BUFFERSIZE, 1)    # Verarbeitungszeit maximal 1ms

    while True:                 # While-Schleife, damit das Programm per Knopfdruck geschlossen werden kann

        _, img = cam.read()                                 # Auslesen der Kamera
        # img = img[100:200, 100:200]                       # Zuschneiden des Bildes

        cv.imshow('image', img)

        if cv.waitKey(1) == ord("0"):  # Abbruchbedingung der Schleife festgelegt als Knopfdruck 0
            break

    cam.release()  # Freigeben der Kamera für andere Zwecke
    cv.destroyAllWindows()  # Schließen aller Fenster, die durch Anwendung geöffnet wurden.


