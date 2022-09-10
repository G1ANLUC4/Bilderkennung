def Kreiserkennung(Aufloesung, Mindestabstand, Kantenwert, Rundheit, MinRadius, MaxRadius):

    import cv2 as cv
    import numpy as np

    template = cv.imread('C:\\Users\\giann\\PycharmProjects\\Projektarbeit\\Fotos\\Testbild.png', 0)
    cv.imshow("Vorgabe", template)

    while True:

        circles = cv.HoughCircles(template, cv.HOUGH_GRADIENT,
                                  Aufloesung, Mindestabstand,
                                  param1=Kantenwert, param2=Rundheit,
                                  minRadius=MinRadius, maxRadius=MaxRadius)

        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                cv.circle(template, (i[0], i[1]), i[2], (255, 0, 0), 5)
                cv.circle(template, (i[0], i[1]), 1, (0, 0, 0), 5)
                print(i[0], i[1])

        cv.imshow('Kreiserkennung', template)

        if cv.waitKey(1) == ord("0"):
            break

    cv.destroyAllWindows()
