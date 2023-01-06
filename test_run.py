def test(cam):
    import cv2 as cv

    # Only to test codefragments, not relevant for normal runs

    cam = cv.VideoCapture(cam)

    while True:

        _, img = cam.read()
        img = img[186:250, 100:500]         # Cutting the picture to only show the track
        cv.imshow('image', img)

        if cv.waitKey(1) == ord("0"):
            break

    cv.destroyAllWindows()
