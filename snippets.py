def Unbekannt():

    import numpy as np
    import cv2 as cv

    cap = cv.VideoCapture(1)
    cap.set(cv.CAP_PROP_BUFFERSIZE, 1)

    while True:
        ret, frame = cap.read()
        # frame = frame[190:250, :]      # cropping & scaling
        # frame = cv.resize(frame,(int(frame.shape[1]*0.7),int(frame.shape[0]*0.7)),interpolation=cv.INTER_AREA)

        src_img = frame.astype(np.uint8)
        color_img = src_img
        src_img = cv.cvtColor(src_img, cv.COLOR_BGR2GRAY)
        cv.imshow('orig', src_img)

        # apply blurring to reduce false detections
        src_img = cv.medianBlur(src_img, 3)
        # apply otsu threshold
        thresh = cv.threshold(src_img, 100, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

        # morphological operations
        kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
        opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=3)

        # find contours
        contours = cv.findContours(opening, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
        contours = contours[0] if len(contours) == 2 else contours[1]
        for c in contours:
            peri = cv.arcLength(c, True)
            approx = cv.approxPolyDP(c, 0.1 * peri, True)
            area = cv.contourArea(c)
            if len(approx) > 3 and area > 10 and area < 500000:
                ((x, y), r) = cv.minEnclosingCircle(c)
                cv.circle(color_img, (int(x), int(y)), int(r), (36, 255, 12), 2)
                # cv.drawContours(color_img, c, -1, (36, 255, 12), 3)

        # cv.imshow('thresh',thresh)
        cv.imshow('opening', opening)
        cv.imshow('circles detected', color_img)

        if cv.waitKey(1) == ord("0"):  # Abbruchbedingung der Schleife festgelegt als Knopfdruck 0
            break

    cap.release()
    cv.destroyAllWindows()
