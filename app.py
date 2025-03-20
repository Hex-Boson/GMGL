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

#Funktionen
def neuesSpielbrett(hoehe,breite):
    print(textfeldHoehe.get(),textfeldBreite.get())
    global spielbrett
    spielbrett=sb.Spielbrett(hoehe,breite)
def zufaelligFuellen():
    spielbrett.zufaellig_fuellen()

ueberschrift=tk.Label(root,text="GMGL")
ueberschrift.grid(column=0,row=0)

#Display
screen=tk.Canvas(root,width=960,height=540,bg="black")
screen.grid(row=2,columnspan=40)


#Eingabefeld für Spielbrettgröße
eingabeHoehe=tk.Entry(root,width=5,textvariable=textfeldHoehe)
eingabeHoehe.grid(column=0,row=4)
eingabeBreite=tk.Entry(root,width=5,textvariable=textfeldBreite)
eingabeBreite.grid(column=1,row=4)

#Buttons
#button für neues Spielbrett
neuesSpielbrettButton = tk.Button(text="neues Spielbrett",command=neuesSpielbrett(textfeldHoehe.get(),textfeldBreite.get()))
neuesSpielbrettButton.grid(column=2,row=4)
#button für zufälliges erschaffen von Leben
zufaelligFuellenButton=tk.Button(text="zufällig füllen",command=zufaelligFuellen())
zufaelligFuellenButton.grid(column=3,row=4)

root.mainloop()