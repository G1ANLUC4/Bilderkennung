def circles(camera, dp, minDist, edgeValue, roundness, minRadius, maxRadius):
    import cv2 as cv
    import numpy as np
    import datetime as dt

    cam = cv.VideoCapture(camera)           # Access the right camera
    cam.set(cv.CAP_PROP_BUFFERSIZE, 1)      # Setting the buffersize to 1ms

    referencetime = dt.datetime.now()       # Using the time of the start as reference to measure the time of one cycle

    while True:                             # While-loop, can be broken by pressing "0"

        if cv.waitKey(1) == ord("1"):       # By pressing "1" you can output the following string
            print("Start of the dataset")   # in the console

        _, img = cam.read()                 # Reading the camera
        img = img[200:250, 100:500]         # Cutting the picture to only show the track

        # Overlaying rectangles to cover screws and the attachment
        cv.rectangle(img, (175, 0), (250, 3), (255, 255, 255), 10)
        cv.rectangle(img, (150, 34), (225, 50), (255, 255, 255), 10)
        cv.rectangle(img, (0, 0), (500, 40), (255, 255, 255), 10)

        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)          # Converting the picture into grayscale
        # blurr = cv.bilateralFilter(gray, 7, 60, 80)       # Optional blurring of the picture
        contur = cv.Canny(gray, 30, 100)                    # Using the Canny-Algorithm to show the contur (optional)

        # Use of the function "HoughCircles"
        detected = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, dp, minDist, param1=edgeValue, param2=roundness,
                                   minRadius=minRadius, maxRadius=maxRadius)

        if detected is not None:

            detected = np.uint16(np.around(detected))   # Converting the detected circles into u-int

            for i in detected[0, :]:                    # Extracting only the centers of the circles

                # picture, center, radius, color, thickness
                cv.circle(img, (i[0], i[1]), i[2], (255, 0, 0), 2)      # Drawing the outer circle
                cv.circle(img, (i[0], i[1]), 1, (0, 0, 0), 2)           # Drawing the center

                scale = (i[0] - 202) * (80 / 365)       # Converting pixels into cm
                now = dt.datetime.now()                 # Determining the actual time
                delta = now - referencetime             # Subtract times to get the passed timedelta

                # Outputting the time and position in the console
                print(str(delta).replace('0:00:', '').replace('.', ','), str(scale).replace('.', ','))

        cv.imshow('contur_detection', img)              # Showing the picture with detected circles
        cv.imshow('canny', contur)                      # Showing the contur (optional)

        if cv.waitKey(1) == ord("0"):                   # Breaking out of the loop by pressing "0"
            break

    cam.release()                                       # Releasing the camera
    cv.destroyAllWindows()                              # Closes all windows
