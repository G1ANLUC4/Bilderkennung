import houghcircles as hc
import color as clr
import contrast as cst
import depth_estimation as de
import mobilenetki as ki
import matching as tm
import testlauf as tl

# Hinweis: Die Ausführung des Codes kann mit Drücken der Taste "0" beendet werden.

# Hier Methodenauswahl über Änderung des int-Wertes: (Legende siehe unten)
Methode = 3
# Auswahl der Kamera, wobei 0 --> Innenkamera und 1 --> Außenkamera
Cam = 1

if Methode == 1:
    print("HoughCircles")
    hc.Kreiserkennung(Cam, 2, 400, 250, 20, 8, 12)

    # Parameter hierbei sind:
    # Aufloesung        -->     Verhältnis zwischen Framerate und Algorithmus-Durchführung
    # Mindestabstand    -->     Mindestabstand zwischen den Zentren der zu erkennenden Kreise
    # Kantenwert        -->     Schwellenwert der an den Canny-Algorithmus weitergegeben wird (Matrixauflösung)
    # Rundheit          -->     Je kleiner dieser Wert, desto genauer müssen die Kreise sein, um erkannt zu werden
    # MinRadius         -->     Kleinster Kreisradius, ab dem der Kreis gesucht wird
    # MaxRadius         -->     Größter Kreisradius, bis zu dem der Kreis gesucht werden soll

elif Methode == 2:
    print("ColorRecognition")
    # Verschiedene Versionen für andere Ballfarben
    clr.Farberkennung(Cam, 0, 10, 150, 255, 150, 255)  # rot
    # clr.Farberkennung(Cam, 0, 360, 0, 120, 0, 120)          # schwarz

    # Parameter hierbei sind:
    # MinWinkel         -->     Unterer Winkel der Farbe im HSV-Modell, ab dem gesucht wird
    # MaxWinkel         -->     Oberer Winkel der Farbe im HSV-Modell, ab dem gesucht wird
    # MinSaettigung     -->     Minimale Saettigung, ab der erkannt werden soll
    # MaxSaettigung     -->     Maximale Saettigung, ab der erkannt werden soll
    # MinHelligkeit     -->     Untere Helligkeit, ab der erkannt werden soll
    # MaxHelligkeit     -->     Obere Helligkeit, ab er erkannt werden soll

elif Methode == 3:
    print("Kontrasterkennung")
    cst.Kontrasterkennung(Cam, 150, 125, 4, 1, 40, 300)

    # Parameter hierbei sind:
    # Untergrenze       -->     unterer Grenzwert, ab dem ein Pixel weiß dargestellt wird
    # Obergrenze        -->     oberer Grenzwert, bis zu dem ein Pixel weiß dargestellt wird
    # Ordnung           -->     Größe der Ellipsen-Maske, mit der gesucht wird
    # Iterationen       -->     Anzahl der Iterationen, mit der die Bit-Maske durchläuft
    # MinFlaeche        -->     Minimale Fläche des Kreises, der erkannt werden soll
    # MaxFlaeche        -->     Maximale Fläche des Kreises, der erkannt werden soll

elif Methode == 4:
    print("Template-Matching")
    tm.TemplateMatching(Cam)

elif Methode == 5:
    print("Tiefenerkennung")
    de.Tiefenerkennung(Cam, 1, 2000, 100, 0.9, 40, 170)

    # Parameter hierbei sind:
    # Aufloesung        -->     Verhältnis zwischen Framerate und Algorithmus-Durchführung
    # Mindestabstand    -->     Mindestabstand zwischen den Zentren der zu erkennenden Kreise
    # Kantenwert        -->     Schwellenwert der an den Canny-Algorithmus weitergegeben wird (Matrixauflösung)
    # Rundheit          -->     Je kleiner dieser Wert, desto genauer müssen die Kreise sein, um erkannt zu werden
    # MinRadius         -->     Kleinster Kreisradius, ab dem der Kreis gesucht wird
    # MaxRadius         -->     Größter Kreisradius, bis zu dem der Kreis gesucht werden soll

elif Methode == 6:
    print("Mobilenet-KI")
    ki.KuenstlicheIntelligenz(Cam)

elif Methode == 7:
    print("Testlauf")
    tl.Kreiserkennung(7, 2000, 100, 0.9, 40, 170)

else:
    print("Bitte wählen Sie eine gültige Methode aus...")
