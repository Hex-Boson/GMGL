#Gabriel

import random       # Bibliothek zum erstellen zufälliger Zahlen
import numpy as np  # Bibliothek für effiziente numerische Berechnungen
#import time         # Zum Einfügen von Verzögerungen zwischen den Schritten
#import os           # Für das Löschen des Terminalbildschirms zur besseren Darstellung

class Spielbrett:
    def __init__(self, hoehe, breite):
        self.breite = breite                                   # Anzahl der Spalten des Spielfelds
        self.hoehe = hoehe                                     # Anzahl der Zeilen des Spielfelds
        self.spielfeld = np.zeros((hoehe, breite), dtype=int)  # Erstellt ein leeres Spielfeld (nur Nullen)
    
    def zufaellig_fuellen(self):                                # Zufällige 0-1-Verteilung für lebende/tote Zellen
        for y in range(0,len(self.spielfeld),1):
            for x in range(0,len(self.spielfeld[y]),1):
                self.spielfeld[y][x]=random.randint(0,1)
    
    def zuruecksetzen(self):
        self.spielfeld = np.zeros((self.hoehe, self.breite), dtype=int)

def zufaelligFuellen(spielbrett):
    spielbrett.zufaellig_fuellen()
# Beispielhafte Nutzung
#game = Spielbrett()  # Erstellt ein Spielfeld mit 20x10 Zellen
#game.breite=20
#game.hoehe=10
#game.zufaellig_fuellen()   # Füllt das Spielfeld zufällig mit lebenden Zellen
#game.starte_simulation()   # Startet die Simulation