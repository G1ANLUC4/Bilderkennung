def Unbekannt():

    import numpy as np
    import cv2 as cv

    cam = cv.VideoCapture(1)

    while True:

        if cv.waitKey(1) == ord("0"):  # Abbruchbedingung der Schleife festgelegt als Knopfdruck 0
            break

    cam.release()
    cv.destroyAllWindows()
