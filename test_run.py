def test(cam):
    import cv2 as cv

    # Only to test codefragments, not relevant for normal runs

    cam = cv.VideoCapture(cam)

    while True:

        _, img = cam.read()
        cv.imshow('picture', img)

        if cv.waitKey(1) == ord("0"):
            break

    cv.destroyAllWindows()
