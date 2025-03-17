import numpy as np  # Bibliothek für effiziente numerische Berechnungen
import time         # Zum Einfügen von Verzögerungen zwischen den Schritten
import os           # Für das Löschen des Terminalbildschirms zur besseren Darstellung

class Spielbrett:
    def _init_(self, breite, hoehe):
        self.breite = breite                                   # Anzahl der Spalten des Spielfelds
        self.hoehe = hoehe                                     # Anzahl der Zeilen des Spielfelds
        self.spielfeld = np.zeros((hoehe, breite), dtype=int)  # Erstellt ein leeres Spielfeld (nur Nullen)
    
    def zufaellig_fuellen(self):
        self.spielfeld = np.random.randint(2, size=(self.hoehe, self.breite))   # Zufällige 0-1-Verteilung für lebende/tote Zellen
    
    def zeige_spielfeld(self):
        os.system('cls' if os.name == 'nt' else 'clear')                        # Löscht den Bildschirm für eine saubere Darstellung
        for zeile in self.spielfeld:
            print("".join("█" if zelle else " " for zelle in zeile))            # Gibt das Spielfeld mit Symbolen aus (█ für lebendig, Leerzeichen für tot)
    
    def naechste_generation(self):
        neues_spielfeld = np.copy(self.spielfeld)                           # Erstellt eine Kopie des aktuellen Spielfelds
        for y in range(self.hoehe):                                         # Geht jede Zeile durch
            for x in range(self.breite):                                    # Geht jede Spalte durch
                # Zählt die lebenden Nachbarn der aktuellen Zelle (8 Nachbarn im 3x3-Umfeld)
                nachbarn = np.sum(self.spielfeld[max(0, y-1):min(self.hoehe, y+2), max(0, x-1):min(self.breite, x+2)]) - self.spielfeld[y, x]
                
                # Regeln von Conway's Game of Life
                if self.spielfeld[y, x] == 1 and (nachbarn < 2 or nachbarn > 3):  # Zelle stirbt an Einsamkeit oder Überbevölkerung
                    neues_spielfeld[y, x] = 0
                elif self.spielfeld[y, x] == 0 and nachbarn == 3:                 # Tote Zelle wird durch genau 3 Nachbarn lebendig
                    neues_spielfeld[y, x] = 1
        self.spielfeld = neues_spielfeld  # Aktualisiert das Spielfeld
    
    def starte_simulation(self, schritte=100, verzögerung=0.1):
        for _ in range(schritte):        # Führt die Simulation für eine festgelegte Anzahl von Schritten aus
            self.zeige_spielfeld()       # Zeigt das aktuelle Spielfeld an
            self.naechste_generation()   # Berechnet die nächste Generation
            time.sleep(verzögerung)      # Wartet kurz für eine flüssige Darstellung

# Beispielhafte Nutzung
game = Spielbrett()  # Erstellt ein Spielfeld mit 20x10 Zellen
game.breite=20
game.hoehe=10
game.zufaellig_fuellen()   # Füllt das Spielfeld zufällig mit lebenden Zellen
game.starte_simulation()   # Startet die Simulation