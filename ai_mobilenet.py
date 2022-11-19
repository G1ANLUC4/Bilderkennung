def ai(camera):

    # Zuweisung der KI-Klassen mit Namen
    objectsnames = {0: 'background',
                    1: 'person', 2: 'bicycle', 3: 'car', 4: 'motorcycle', 5: 'airplane', 6: 'bus',
                    7: 'train', 8: 'truck', 9: 'boat', 10: 'traffic light', 11: 'fire hydrant',
                    13: 'stop sign', 14: 'parking meter', 15: 'bench', 16: 'bird', 17: 'cat',
                    18: 'dog', 19: 'horse', 20: 'sheep', 21: 'cow', 22: 'elephant', 23: 'bear',
                    24: 'zebra', 25: 'giraffe', 27: 'backpack', 28: 'umbrella', 31: 'handbag',
                    32: 'tie', 33: 'suitcase', 34: 'frisbee', 35: 'skis', 36: 'snowboard',
                    37: 'sports ball', 38: 'kite', 39: 'baseball bat', 40: 'baseball glove',
                    41: 'skateboard', 42: 'surfboard', 43: 'tennis racket', 44: 'bottle',
                    46: 'wine glass', 47: 'cup', 48: 'fork', 49: 'knife', 50: 'spoon',
                    51: 'bowl', 52: 'banana', 53: 'apple', 54: 'sandwich', 55: 'orange',
                    56: 'broccoli', 57: 'carrot', 58: 'hot dog', 59: 'pizza', 60: 'donut',
                    61: 'cake', 62: 'chair', 63: 'couch', 64: 'potted plant', 65: 'bed',
                    67: 'dining table', 70: 'toilet', 72: 'tv', 73: 'laptop', 74: 'mouse',
                    75: 'remote', 76: 'keyboard', 77: 'cell phone', 78: 'microwave', 79: 'oven',
                    80: 'toaster', 81: 'sink', 82: 'refrigerator', 84: 'book', 85: 'clock',
                    86: 'vase', 87: 'scissors', 88: 'teddy bear', 89: 'hair drier', 90: 'toothbrush'}

    import cv2 as cv
    import datetime as dt

    # Selection of the used model
    model = cv.dnn.readNetFromTensorflow(
        'C:\\Users\\giann\\PycharmProjects\\Projektarbeit\\models\\frozen_inference_graph.pb',
        'C:\\Users\\giann\\PycharmProjects\\Projektarbeit\\models\\ssd_mobilenet_v2_coco_2018_03_29.pbtxt')

    cam = cv.VideoCapture(camera)           # Access the right camera
    # cam.set(cv.CAP_PROP_BUFFERSIZE, 1)      # Setting the buffersize to 1ms

    referencetime = dt.datetime.now()       # Using the time of the start as reference to measure the time of one cycle

    while True:                             # While-loop, can be broken by pressing "0"

        if cv.waitKey(1) == ord("1"):       # By pressing "1" you can output the following string
            print("Start of the dataset")   # in the console

        _, img = cam.read()                 # Reading the camera
        # img = img[200:250, 100:500]         # Cutting the picture to only show the track
        height, width, _ = img.shape        # Saving the measures of the templates

        blob = cv.dnn.blobFromImage(img, size=(width, height), swapRB=True)     # Creating a blob
        model.setInput(blob)                                                    # Using blob

        # Matching class-ID with name
        def id_Object_class(classid, classes):
            for key_id, classname in classes.items():
                if classid == key_id:
                    return classname

        output = model.forward()        # Getting output of the ai-model

        if len(output) == 0:                    # In case no object was found
            now = dt.datetime.now()             # Determining the actual time
            delta = now - referencetime         # Subtract times to get the passed timedelta

            # Outputting the time and an empty position in the console
            print(str(delta).replace('0:00:', '').replace('.', ','), "-99,99")

        else:
            counter = 0     # Creating a counter, to check, if the same time had an output

            for detection in output[0, 0, :, :]:                            # Process every detection
                confidence = detection[2]                                   # Extracting the confidence of the detection
                if confidence > .35:                                        # Proceed only, if for great confidence
                    class_id = detection[1]                                 # Connecting Class-ID
                    class_name = id_Object_class(class_id, objectsnames)    # Connecting Class-Name

                    box_x = detection[3] * width           # Preparations for later to draw the rectangles
                    box_y = detection[4] * height
                    box_width = detection[5] * width
                    box_height = detection[6] * height

                    # Drawing a rectangle around the ball
                    cv.rectangle(img, (int(box_x), int(box_y)), (int(box_width), int(box_height)),
                                 (23, 230, 210), thickness=1)

                    # Labeling the rectangle with class-name
                    cv.putText(img, class_name, (int(box_x), int(box_y + .005 * height)),
                               cv.FONT_HERSHEY_SIMPLEX, (.0005 * width), (0, 0, 255))

                    now = dt.datetime.now()         # Determining the actual time
                    delta = now - referencetime     # Subtract times to get the passed timedelta

                    # Outputting the time and an empty position in the console
                    print(str(delta).replace('0:00:', '').replace('.', ','),
                          str(detection[3]*width).replace('.', ','), class_name)

                    counter = 1     # Set the counter to 1

                else:
                    if counter == 0:
                        now = dt.datetime.now()         # Determining the actual time
                        delta = now - referencetime     # Subtract times to get the passed timedelta

                        # Outputting the time and an empty position in the console
                        print(str(delta).replace('0:00:', '').replace('.', ','), "-99,99")

                        counter = 1  # Set the counter to 1

        cv.imshow('ai_mobilenet', img)          # Showing the picture with detected circles

        if cv.waitKey(1) == ord("0"):           # Breaking out of the loop by pressing "0"
            break

    cam.release()                               # Releasing the camera
    cv.destroyAllWindows()                      # Closes all windows
