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
textfeldHoehe=tk.IntVar()
textfeldBreite=tk.IntVar()
skalierungsfaktor=int(round((960/(textfeldBreite.get()+1)+540/(textfeldBreite.get()+1))/2))
global spielbrett
spielbrett=sb.Spielbrett(10,20)
global spieler
spieler=[]

#Funktionen
def neuesSpielbrett():
    hoehe=textfeldHoehe.get()
    breite=textfeldBreite.get()
    global spielbrett
    spielbrett=sb.Spielbrett(hoehe,breite)
def zufaelligFuellen():
    spielbrett.zufaellig_fuellen()
    spielerErstellen()
    test=tk.Label(root,text="test")
    test.grid(column=5,row=0)
def spielerErstellen():
    for y in range(0,len(spielbrett.spielfeld),1):
        for x in range(0,len(spielbrett.spielfeld[y]),1):
            spieler.append(sp.Spieler(x,y,spielbrett.spielfeld[y][x]))

def spielbrettZeichnen():
    screen=tk.Canvas(root,width=textfeldBreite.get()*skalierungsfaktor,height=textfeldHoehe.get()*skalierungsfaktor,bg="black")
    screen.grid(row=2,)
    for y in range(0,len(spielbrett.spielfeld),1):
        for x in range(0,len(spielbrett.spielfeld[y]),1):
            screen.create_rectangle(x*skalierungsfaktor,y*skalierungsfaktor,skalierungsfaktor,skalierungsfaktor,fill="blue")

#Überschrift
ueberschrift=tk.Label(root,text="GMGL")
ueberschrift.grid(column=0,row=0)

#Display
screen=tk.Canvas(root,width=textfeldBreite.get()*skalierungsfaktor,height=textfeldHoehe.get()*skalierungsfaktor,bg="black")
screen.grid(row=2,)

#Eingabefeld für Spielbrettgröße
eingabeHoehe=tk.Entry(root,width=5,textvariable=textfeldHoehe)
eingabeHoehe.grid(column=0,row=4)
eingabeBreite=tk.Entry(root,width=5,textvariable=textfeldBreite)
eingabeBreite.grid(column=1,row=4)

#Buttons
#button für neues Spielbrett
neuesSpielbrettButton = tk.Button(text="neues Spielbrett",command=neuesSpielbrett)
neuesSpielbrettButton.grid(column=2,row=4)
#button für zufälliges erschaffen von Leben
zufaelligFuellenButton=tk.Button(text="zufällig füllen",command=zufaelligFuellen)
zufaelligFuellenButton.grid(column=3,row=4)

root.mainloop()