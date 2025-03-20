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
def getHoehe():
    if not eingabeHoehe.getint()>=0:
        return 10
    else:
        return eingabeHoehe.getint()
def getBreite():
    if not eingabeBreite.getint()>=0:
        return 20
    else:
        return eingabeBreite.getint()
#Spiel
ueberschrift=tk.Label(root,text="GMGL")
ueberschrift.grid()

#Display
screen=tk.Canvas(root,width=960,height=540)

#Eingabefeld für Spielbrettgröße
eingabeHoehe=tk.Entry(root,width=15)
eingabeHoehe.grid(column=0,row=1)
eingabeBreite=tk.Entry(root,width=15)
eingabeBreite.grid(column=2,row=1)

#button für neues Spielbrett
neuesSpielbrettButton = tk.Button(text="neues Spielbrett",command=neuesSpielbrett(10,20))
neuesSpielbrettButton.grid(column=4,row=1)
#button für zufälliges erschaffen von Leben
zufaelligFuellenButton=tk.Button(text="zufällig füllen",command=zufaelligFuellen())
zufaelligFuellenButton.grid()
print(eingabeBreite.get())
root.mainloop()