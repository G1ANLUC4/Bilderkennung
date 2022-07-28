import houghcircles as hc
import colorrecognition as cr

# Hinweis: Die Ausführung des Codes kann mit Drücken der Taste "0" beendet werden.
# Hier Methodenauswahl über Änderung des int-Wertes: (Legende siehe unten)
Methode = 2

if Methode == 1:
    print("HoughCircles")
    hc.Kreiserkennung(7, 2000, 100, 0.9, 40, 170)
    # Parameter hierbei sind:

    # Aufloesung        -->     Verhältnis zwischen Framerate und Algorithmus-Durchführung
    # Mindestabstand    -->     Mindestabstand zwischen den Zentren der zu erkennenden Kreise
    # Kantenwert        -->     Schwellenwert der an den Canny-Algorithmus weitergegeben wird (Matrixauflösung)
    # Perfektion        -->     Je kleiner dieser Wert, desto genauer müssen die Kreise sein, um erkannt zu werden
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

elif Methode == 4:
    print("Methode 4 noch nicht verfügbar!")

elif Methode == 5:
    print("Methode 5 noch nicht verfügbar!")

else:
    print("Bitte wählen Sie eine gültige Methode aus...")
