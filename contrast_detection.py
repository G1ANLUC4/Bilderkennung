def contrast(camera, threshold, maxval, order, iterations, min_area, max_area):
    import cv2 as cv
    import numpy as np
    import datetime as dt

    # Presetting standard parameters for later
    xval = 0
    yval = 0
    rval = 0
    x = 0

    cam = cv.VideoCapture(camera)           # Access the right camera
    cam.set(cv.CAP_PROP_BUFFERSIZE, 1)      # Setting the buffersize to 1ms

    referencetime = dt.datetime.now()       # Using the time of the start as reference to measure the time of one cycle

    while True:                             # While-loop, can be broken by pressing "0"

        if cv.waitKey(1) == ord("1"):       # By pressing "1" you can output the following string
            print("Start of the dataset")   # in the console

        _, img = cam.read()                 # Reading the camera
        img = img[216:226, 110:490]         # Cutting the picture to only show the track

        src_img = img.astype(np.uint8)                      # Converting the picture
        gray = cv.cvtColor(src_img, cv.COLOR_BGR2GRAY)      # Converting into grayscale
        blur = cv.medianBlur(gray, 3)                       # Blurring the picture

        # The threshold-analysis divides the picture into black/white respectively 1/0
        thresh = cv.threshold(blur, threshold, maxval, cv.THRESH_BINARY_INV)[1]

        structure = cv.getStructuringElement(cv.MORPH_ELLIPSE, (order, order))              # Creating bitmask
        result = cv.morphologyEx(thresh, cv.MORPH_OPEN, structure, iterations=iterations)   # Appy bitmask

        # Filtering all contours on straight lines
        contur = cv.findContours(result, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

        if len(contur) == 2:        # Distinction for different numbers of contours
            contur = contur[0]
        else:
            contur = contur[1]

        distance = 16               # Setting a distance outside the picture to start searching for circles

        for c in contur:
            area = cv.contourArea(c)                    # Extracting the area of the contur

            if min_area < area < max_area:              # Filter the contur by area
                ((x, y), r) = cv.minEnclosingCircle(c)  # Enclose the contur with a circle

                if abs(15 - y) < distance:  # Sorting the contours to find the most central one (y-axis)
                    distance = 15 - y       # If the new contur is more central, then replace the distance
                    xval = int(x)           # Save the parameters of the most central circle
                    yval = int(y)
                    rval = int(r)

        cv.circle(img, (int(xval), int(yval)), int(rval), (255, 0, 0), 2)       # Drawing the outer circle
        cv.circle(img, (int(xval), int(yval)), 1, (0, 0, 0), 2)                 # Drawing the center

        scale = (int(xval) - 190) * (80 / 380)      # Converting pixels into cm
        now = dt.datetime.now()                     # Determining the actual time
        delta = now - referencetime                 # Subtract times to get the passed timedelta

        # Outputting the time and position in the console
        print(str(delta).replace('0:00:', '').replace('.', ','), str(scale).replace('.', ','))

        cv.imshow('contrast_detection', img)        # Showing the picture with detected circles
        # cv.imshow('circles detected', gray)       # Showing the picture in grayscale
        # cv.imshow('blur', blur)                   # Showing the blurred picture
        # cv.imshow('thresh_analysis', thresh)      # Showing the thresh_analysis result
        cv.imshow('structures', result)             # Showing the result of the bitmask

        if cv.waitKey(1) == ord("0"):               # Breaking out of the loop by pressing "0"
            break

    cam.release()                                   # Releasing the camera
    cv.destroyAllWindows()                          # Closes all windows
