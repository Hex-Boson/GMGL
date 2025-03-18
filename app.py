#Klassen importieren
from Klassen import Spielbrett as sb
from Klassen import Spieler as sp
#Bibiliotheken importieren
import tkinter as tk
import time

#Fenster erstellen
root=tk.Tk()
root.title("GMGL")
root.geometry("1280x720")

#Variablen
spieler=[]
#Funktionen
def neuesSpielbrett(hoehe,breite):
    global spielbrett
    spielbrett=sb.Spielbrett(hoehe,breite)
def zufaelligFuellen():
    spielbrett.zufaellig_fuellen()

#Spiel
ueberschrift=tk.Label(root,text="GMGL")
ueberschrift.grid()

#Display
screen=tk.Canvas(root,width=960,height=540)

#button für neues Spielbrett
neuesSpielbrettButton = tk.Button(
                   text="neues Spielbrett",command=neuesSpielbrett(10,20))
neuesSpielbrettButton.grid()
#button für zufälliges erschaffen von Leben
zufaelligFuellenButton=tk.Button(text="zufällig füllen",command=zufaelligFuellen())
zufaelligFuellenButton.grid()

root.mainloop()