def depth(camera, dp, minDist, edgeValue, roundness, minRadius, maxRadius):
    import numpy as np
    import cv2 as cv
    import datetime as dt

    # Selection of the used model
    model = cv.dnn.readNet('C:\\Users\\giann\\PycharmProjects\\Projektarbeit\\models\\model-small.onnx')

    cam = cv.VideoCapture(camera)           # Access the right camera
    # cam.set(cv.CAP_PROP_BUFFERSIZE, 1)      # Setting the buffersize to 1ms

    referencetime = dt.datetime.now()       # Using the time of the start as reference to measure the time of one cycle

    while True:                             # While-loop, can be broken by pressing "0"

        if cv.waitKey(1) == ord("1"):       # By pressing "1" you can output the following string
            print("Start of the dataset")   # in the console

        _, img = cam.read()                 # Reading the camera
        img = img[208:228, 100:500]         # Cutting the picture to only show the track
        h, w, _ = img.shape                 # Saving the measures

        # Creating a blob
        blob = cv.dnn.blobFromImage(img, 1 / 255., (256, 256), (123.675, 116.28, 103.53), True, False)

        model.setInput(blob)                # Using blob
        output = model.forward()            # Getting output of the ai-model

        output = output[0, :, :]                   # Save the output array
        output = cv.resize(output, (w, h))         # Cutting output to original size

        # Normalising output into different types
        outfordm = cv.normalize(output, None, 0, 1, norm_type=cv.NORM_MINMAX, dtype=cv.CV_32F)
        output = cv.normalize(outfordm, None, 0, 255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8U)

        # Use of the function "HoughCircles"
        circles = cv.HoughCircles(output, cv.HOUGH_GRADIENT, dp, minDist, param1=edgeValue, param2=roundness,
                                  minRadius=minRadius, maxRadius=maxRadius)

        if circles is not None:
            circles = np.uint16(np.around(circles))                 # Converting the detected circles into u-int
            for i in circles[0, :]:                                 # Extracting only the centers of the circles
                # picture, center, radius, color, thickness
                cv.circle(img, (i[0], i[1]), i[2], (255, 0, 0), 2)      # Drawing the outer circle
                cv.circle(img, (i[0], i[1]), 1, (0, 0, 0), 2)           # Drawing the center

                scale = (i[0]-203)*(40/185)         # Converting pixels into cm
                now = dt.datetime.now()             # Determining the actual time
                delta = now - referencetime         # Subtract times to get the passed timedelta

                # Outputting the time and position in the console
                print(str(delta).replace('0:00:', '').replace('.', ','), str(scale).replace('.', ','))
        else:
            now = dt.datetime.now()  # Determining the actual time
            delta = now - referencetime  # Subtract times to get the passed timedelta
            print(str(delta).replace('0:00:', '').replace('.', ','), '-99,99')

        cv.imshow('depth_estimation', img)          # Showing the picture with detected circles
        cv.imshow('depth_map', outfordm)            # Showing the Depth Map

        if cv.waitKey(1) == ord("0"):               # Breaking out of the loop by pressing "0"
            break

    cam.release()                                   # Releasing the camera
    cv.destroyAllWindows()                          # Closes all windows
