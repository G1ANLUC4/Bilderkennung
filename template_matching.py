def matching(camera):
    import cv2 as cv
    import datetime as dt

    # Opening the template
    # a) on my PC
    template = cv.imread('C:\\Users\\giann\\PycharmProjects\\Projektarbeit\\Fotos\\Ballfoto3.png', 0)
    # b) on the Raspberry-Pi
    # template = cv.imread('/home/rus/Desktop/Projektarbeit/Fotos/Ballfoto5.png', 0)

    w, h = template.shape[::-1]         # Saving the measures of the templates
    w = round(w / 2)                    # Halve the width of the template
    h = round(h / 2)                    # Halve the height of the template
    cv.imshow("template", template)     # Showing the template

    cam = cv.VideoCapture(camera)           # Access the right camera
    cam.set(cv.CAP_PROP_BUFFERSIZE, 1)      # Setting the buffersize to 1ms

    referencetime = dt.datetime.now()       # Using the time of the start as reference to measure the time of one cycle

    while True:                             # While-loop, can be broken by pressing "0"

        if cv.waitKey(1) == ord("1"):       # By pressing "1" you can output the following string
            print("Start of the dataset")   # in the console

        _, img = cam.read()                 # Reading the camera
        img = img[207:237, 110:490]         # Cutting the picture to only show the track

        mean = img.mean(axis=0).mean(axis=0)                                    # Taking the average color of the ball
        cv.rectangle(img, (0, 0), (390, 3), (mean[0], mean[1], mean[2]), 7)     # Border the picture with average color
        cv.rectangle(img, (0, 25), (390, 30), (mean[0], mean[1], mean[2]), 7)   # to analyse an even smaller image

        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)                              # Converting into grayscale

        result = cv.matchTemplate(gray, template, cv.TM_CCORR_NORMED)           # Comparing the image with the template

        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)               # Output of the Extrema of the matching
        cv.circle(img, (min_loc[0] + w, min_loc[1] + h), w, (255, 0, 0), 2)     # Drawing a circle around the maximum

        scale = ((min_loc[0] - 190) * (80 / 380))   # Converting pixels into cm
        now = dt.datetime.now()                     # Determining the actual time
        delta = now - referencetime                 # Subtract times to get the passed timedelta

        # Outputting the time and position in the console
        print(str(delta).replace('0:00:', '').replace('.', ','), str(scale).replace('.', ','))

        cv.imshow('template_matching', img)     # Showing the picture with detected circles
        cv.imshow('matching', result)           # Showing the matching result

        if cv.waitKey(1) == ord("0"):           # Breaking out of the loop by pressing "0"
            break

    cam.release()                               # Releasing the camera
    cv.destroyAllWindows()                      # Closes all windows
