import houghcircles as hc
import color as cr
import contrast as m3
import methode4 as m4
import methode5 as m5
import snippets as sn

# Hinweis: Die Ausführung des Codes kann mit Drücken der Taste "0" beendet werden.
# Hier Methodenauswahl über Änderung des int-Wertes: (Legende siehe unten)
Methode = 3

if Methode == 1:
    print("HoughCircles")
    hc.Kreiserkennung(7, 2000, 100, 0.9, 40, 170)
    # Parameter hierbei sind:

    # Aufloesung        -->     Verhältnis zwischen Framerate und Algorithmus-Durchführung
    # Mindestabstand    -->     Mindestabstand zwischen den Zentren der zu erkennenden Kreise
    # Kantenwert        -->     Schwellenwert der an den Canny-Algorithmus weitergegeben wird (Matrixauflösung)
    # Rundheit          -->     Je kleiner dieser Wert, desto genauer müssen die Kreise sein, um erkannt zu werden
    # MinRadius         -->     Kleinster Kreisradius, ab dem der Kreis gesucht wird
    # MaxRadius         -->     Größter Kreisradius, bis zu dem der Kreis gesucht werden soll

    # Quelle: https://docs.opencv.org/4.x/dd/d1a/group__imgproc__feature.html#ga47849c3be0d0406ad3ca45db65a25d2d

elif Methode == 2:
    print("ColorRecognition")
    cr.Farberkennung(140, 179, 50, 255, 50, 255)
    # Parameter hierbei sind:

    # MinWinkel         -->     Unterer Winkel der Farbe im HSV-Modell, ab dem gesucht wird
    # MaxWinkel         -->     Oberer Winkel der Farbe im HSV-Modell, ab dem gesucht wird
    # MinSaettigung     -->     Minimale Saettigung, ab der erkannt werden soll
    # MaxSaettigung     -->     Maximale Saettigung, ab der erkannt werden soll
    # MinHelligkeit     -->     Untere Helligkeit, ab der erkannt werden soll
    # MaxHelligkeit     -->     Obere Helligkeit, ab er erkannt werden soll

    # Quelle: https://de.acervolima.com/erkennung-einer-bestimmten-farbe-hier-blau-mit-opencv-mit-python/

elif Methode == 3:
    print("Methode 3 noch nicht verfügbar!")
    m3.Kontrasterkennung(100, 255, 5, 3, 1000, 50000)
    # Parameter hierbei sind:

    # Untergrenze       -->     unterer Grenzwert, ab dem ein Pixel weiß dargestellt wird
    # Obergrenze        -->     oberer Grenzwert, bis zu dem ein Pixel weiß dargestellt wird
    # Ordnung           -->     Größe der Ellipsen-Maske, mit der gesucht wird
    # Iterationen       -->     Anzahl der Iterationen, mit der die Bit-Maske durchläuft
    # MinFlaeche        -->     Minimale Fläche des Kreises, der erkannt werden soll
    # MaxFlaeche        -->     Maximale Fläche des Kreises, der erkannt werden soll

    # Quelle: https://docs.opencv.org/4.x/d7/d1b/group__imgproc__misc.html#gaa9e58d2860d4afa658ef70a9b1115576
    # Quelle: https://docs.opencv.org/4.x/d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57
    # Quelle: https://www.wenglor.com/de/Threshold/l/cxmCID148434
    # Quelle: https://docs.opencv.org/3.4/d3/dc0/group__imgproc__shape.html#ga17ed9f5d79ae97bd4c7cf18403e1689a
    # Quelle: https://opencv24-python-tutorials.readthedocs.io/en/latest/
    #         py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html

elif Methode == 4:
    print("Methode 4 noch nicht verfügbar!")
    m4.VierteArt(0)
    # Parameter hierbei sind:

    # Para1             -->     BeispielParameter

    # Quelle: www.url.org

elif Methode == 5:
    print("Methode 5 noch nicht verfügbar!")
    m5.FuenfteArt(0)
    # Parameter hierbei sind:

    # Para1             -->     BeispielParameter

    # Quelle: www.url.org

elif Methode == 6:
    print("Unbekannt Methode")
    sn.Unbekannt()

else:
    print("Bitte wählen Sie eine gültige Methode aus...")
