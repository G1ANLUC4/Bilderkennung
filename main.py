import contur_detection as ctr
import color_detection as clr
import contrast_detection as cst
import depth_estimation as de
import ai_mobilenet as aim
import template_matching as tm
import test_run as tr

# Notice: You can stop the program by pressing "0"

# Choose the method by changing the number corresponding to the entry in the elif-statement
method = 0
# Choose 0 or 1 to change the camera (in some cases it may be 2)
camera = 0

if method == 1:
    print("Using contur_detection:")
    ctr.circles(camera, 2, 400, 250, 20, 8, 12)

    # Parameter hierbei sind:
    # dp        -->     Verhältnis zwischen Framerate und Algorithmus-Durchführung
    # minDist    -->     minDist zwischen den Zentren der zu erkennenden Kreise
    # edgeValue        -->     Schwellenwert der an den Canny-Algorithmus weitergegeben wird (Matrixauflösung)
    # roundness          -->     Je kleiner dieser Wert, desto genauer müssen die Kreise sein, um erkannt zu werden
    # minRadius         -->     Kleinster Kreisradius, ab dem der Kreis gesucht wird
    # maxRadius         -->     Größter Kreisradius, bis zu dem der Kreis gesucht werden soll

elif method == 2:
    print("Using color_detection:")
    clr.color(camera, 50)  # für rot/schwarz ca 50/16

    # Parameter hierbei ist:
    # variance        -->     Werteabstand, um mittlere detektierte Farbe, der als gültig eingestuft wird

elif method == 3:
    print("Using contrast_detection:")
    cst.contrast(camera, 150, 125, 4, 2, 40, 300)  # rot
    # cst.contrast(camera, 95, 125, 4, 2, 40, 320)  # schwarz

    # Parameter hierbei sind:
    # thresh       -->     unterer Grenzwert, ab dem ein Pixel weiß dargestellt wird
    # maxval        -->     oberer Grenzwert, bis zu dem ein Pixel weiß dargestellt wird
    # order           -->     Größe der Ellipsen-Maske, mit der gesucht wird
    # iterations       -->     Anzahl der iterations, mit der die Bit-Maske durchläuft
    # min_area        -->     Minimale Fläche des Kreises, der erkannt werden soll
    # max_area        -->     Maximale Fläche des Kreises, der erkannt werden soll

elif method == 4:
    print("Using template_matching:")
    tm.matching(camera)

elif method == 5:
    print("Using depth_estimation:")
    de.depth(camera, 1, 2000, 100, 0.9, 40, 170)

    # Parameter hierbei sind:
    # dp        -->     Verhältnis zwischen Framerate und Algorithmus-Durchführung
    # minDist    -->     minDist zwischen den Zentren der zu erkennenden Kreise
    # edgeValue        -->     Schwellenwert der an den Canny-Algorithmus weitergegeben wird (Matrixauflösung)
    # roundness          -->     Je kleiner dieser Wert, desto genauer müssen die Kreise sein, um erkannt zu werden
    # minRadius         -->     Kleinster Kreisradius, ab dem der Kreis gesucht wird
    # maxRadius         -->     Größter Kreisradius, bis zu dem der Kreis gesucht werden soll

elif method == 6:
    print("Using ai_mobilenet:")
    aim.ai(camera)

elif method == 7:
    print("Using test_run")
    tr.test(camera)

else:
    print("Please choose an existing method")
    print("1 --> contur_detection")
    print("2 --> color_detection")
    print("3 --> contrast_detection")
    print("4 --> template_matching")
    print("5 --> depth_estimation")
    print("6 --> ai_mobilenet")
    print("7 --> test_run")
