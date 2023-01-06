def color(camera, variance):
    import cv2 as cv
    import numpy as np
    import datetime as dt

    cam = cv.VideoCapture(camera)           # Access the right camera
    # cam.set(cv.CAP_PROP_BUFFERSIZE, 1)    # Setting the buffersize to 1ms

    referencetime = dt.datetime.now()       # Using the time of the start as reference to measure the time of one cycle

    # Taking a picture of the ball to read out the color of the ball
    _, refimg = cam.read()                  # Reading the camera

    refimg = refimg[218:228, 485:495]       # Use this, if the ball is on the right side of the track at start
    # refimg = refimg[218:228, 105:110]     # Use this, if the ball is on the left side of the track at start
    # refimg = refimg[210:230, 290:310]     # Use this, if the ball is in the middle of the track at start

    cv.imshow('color of the ball', refimg)                          # Show the image of the ball
    refimg = cv.cvtColor(refimg, cv.COLOR_BGR2HSV)                  # Converting the image to HSV
    average = refimg.mean(axis=0).mean(axis=0)                      # Taking the average color of the ball
    print("average color", average[0], average[1], average[2])      # Output the average color in the console

    # Opening an interval around the average color to search in the picture
    min_hue = average[0] - variance
    max_hue = average[0] + variance
    min_saturation = average[1] - variance
    max_saturation = average[1] + variance
    min_value = average[2] - variance
    max_value = average[2] + variance

    while True:                             # While-loop, can be broken by pressing "0"

        if cv.waitKey(1) == ord("1"):       # By pressing "1" you can output the following string
            print("Start of the dataset")   # in the console

        _, img = cam.read()                 # Reading the camera
        img = img[200:250, 100:500]         # Cutting the picture to only show the track

        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)    # Converting the picture into HSV

        minimum = np.array([min_hue, min_saturation, min_value])    # setting the lower values
        maximum = np.array([max_hue, max_saturation, max_value])    # setting the upper values
        mask = cv.inRange(hsv, minimum, maximum)                    # Assembling the conditions of the mask
        combination = cv.bitwise_and(img, img, mask=mask)           # Overlaying mask on picture

        points = np.argwhere(mask > 0)     # Reading out every point of the new picture different to black/0

        center, radius = cv.minEnclosingCircle(points)                                  # Drawing circle around points
        cv.circle(img, (int(center[1]), int(center[0])), int(radius), (255, 0, 0), 2)   # Drawing the outer circle
        cv.circle(img, (int(center[1]), int(center[0])), 1, (0, 0, 0), 2)               # Drawing the center

        scale = (center[1] - 202) * (80 / 365)      # Converting pixels into cm
        now = dt.datetime.now()                     # Determining the actual time
        delta = now - referencetime                 # Subtract times to get the passed timedelta

        # Outputting the time and position in the console
        print(str(delta).replace('0:00:', '').replace('.', ','), str(scale).replace('.', ','))

        cv.imshow('color_recognition', img)         # Showing the picture with detected circles
        cv.imshow('HSV-Colorscale', hsv)            # Showing the picture as HSV
        cv.imshow('bitmask', mask)                  # Showing the bitmask
        cv.imshow('filtered', combination)          # Showing the picture after using the mask

        if cv.waitKey(1) == ord("0"):               # Breaking out of the loop by pressing "0"
            break

    cam.release()                                   # Releasing the camera
    cv.destroyAllWindows()                          # Closes all windows
