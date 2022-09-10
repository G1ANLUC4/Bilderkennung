def KuenstlicheIntelligenz(Kamera):

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

    # Auswahl der verwendeten KI-Modelle
    model = cv.dnn.readNetFromTensorflow('models/frozen_inference_graph.pb',
                                         'models/ssd_mobilenet_v2_coco_2018_03_29.pbtxt')

    cam = cv.VideoCapture(Kamera)       # Aufruf der Kamera
    cam.set(cv.CAP_PROP_BUFFERSIZE, 1)  # Verarbeitungszeit maximal 1ms

    while True:                         # While-Schleife, damit das Programm per Knopfdruck geschlossen werden kann

        _, img = cam.read()                 # Auslesen der Kamera
        img = img[200:250, 100:500]         # Zuschneiden des Bildes
        hoehe, breite, farbe = img.shape    # Auslesen der Maße für später

        blob = cv.dnn.blobFromImage(img, size=(hoehe, breite), swapRB=True)     # Erstellen des blobs in rgb
        model.setInput(blob)                                                    # Anwenden des lobs in KI

        print("First Blob: {}".format(blob.shape))          # Ausgabe des zuerst erkannten blobs in Konsole

        def id_Object_class(classid, classes):
            for key_id, classname in classes.items():
                if classid == key_id:
                    return classname                        # Erstellen des Klassennamens laut KI

        output = model.forward()                            # Ausgabe der KI-Ergebnisse

        for detection in output[0, 0, :, :]:                # Jedes erkannte Objekt wird nun verarbeitet
            confidence = detection[2]                       # Zwischenspeicherung der Wahrscheinlichkeit laut KI
            if confidence > .35:                            # Wenn die Wahrscheinlichkeit/Sicherheit der KI über 35 %
                class_id = detection[1]                     # wird der Objektname weitergegeben
                class_name = id_Object_class(class_id, objectsnames)  # Zuweisung der Klasse zum passenden Namen (s. o.)

                print(str(str(class_id) + " " + str(detection[2]) + " " + class_name))  # Konsolenausgabe

                box_x = detection[3] * breite           # Vorbereitungen für Zeichnung der Rechtecke in Ausgabebild
                box_y = detection[4] * hoehe
                box_width = detection[5] * breite
                box_height = detection[6] * hoehe

                cv.rectangle(img, (int(box_x), int(box_y)),         # Zeichnen der Rechtecke in das Kamerabild
                             (int(box_width), int(box_height)),
                             (23, 230, 210),
                             thickness=1)

                cv.putText(img, class_name,                         # Beschriften des Rechtecks mit Name der Klasse
                           (int(box_x), int(box_y + .005 * hoehe)),
                           cv.FONT_HERSHEY_SIMPLEX,
                           (.0005 * breite), (0, 0, 255))

        cv.imshow('Erkennungsabbild', img)      # Anzeigen des Bildes auf Monitor, zur Überwachung

        if cv.waitKey(1) == ord("0"):           # Abbruchbedingung der Schleife festgelegt als Knopfdruck 0
            break

    cam.release()               # Freigeben der Kamera für andere Zwecke
    cv.destroyAllWindows()      # Schließen aller Fenster, die durch Anwendung geöffnet wurden.
