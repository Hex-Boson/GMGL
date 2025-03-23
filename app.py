#Klassen importieren
from Klassen import Spielbrett as sb
from Klassen import Spieler as sp
#Bibiliotheken importieren
import tkinter as tk

#Fenster erstellen
root=tk.Tk()
root.title("GMGL")
root.geometry("1280x720")

#Variablen
canvasBreite=900
canvasHöhe= 500
textfeldHoehe=tk.IntVar(value=10)
textfeldBreite=tk.IntVar(value=20)
spielbrett=sb.Spielbrett(textfeldHoehe.get(),textfeldBreite.get())
spieler=[]
endAnimation=False
global bearbeiten
bearbeiten=False

#Funktionen
#Berechnet Skalierung der Spieler, sodass Spielfeldgröße konstant bleibt
def skalierungsfaktorBerechnen():
    spielerY=textfeldHoehe.get()
    spielerX=textfeldBreite.get()
    spielerBreite=canvasBreite/spielerX
    spielerHoehe=canvasHöhe/spielerY
    return min(spielerBreite,spielerHoehe)

#Erstellt neues Spielbrett, erstellt über weiter Funktionen Spieler und Zeichnet Spielbrett
def neuesSpielbrett():
    global spielbrett
    spielbrett=sb.Spielbrett(textfeldHoehe.get(),textfeldBreite.get())
    spielerErstellen()
    spielbrettZeichnen()

#Füllt Spielbrett zufällig mit Leben
def zufaelligFuellen():
    global endAnimation
    endAnimation=False
    spielbrett.zufaellig_fuellen()
    spielerErstellen()
    spielbrettZeichnen()

#Erstellt Liste mit Spielern
def spielerErstellen():
    global spieler
    spieler.clear()
    for y in range(len(spielbrett.spielfeld)):
        for x in range(len(spielbrett.spielfeld[y])):
            spieler.append(sp.Spieler(x,y,spielbrett.spielfeld[y][x]))

def animationAbbrechen():
    global endAnimation
    endAnimation=True

def animationStarten():
    global endAnimation
    endAnimation=False
    screen.after(1000,spielbrettZeichnen)

#Aktualisiert Status der Spieler und Spielbrett
def spielAktuallisieren():
    for s in spieler:
        s.update(spielbrett.spielfeld)
    for s in spieler:
        spielbrett.spielfeld[s.y][s.x]=s.status

#zeichnet Spielbrett
def spielbrettZeichnen():
    global screen
    if endAnimation:
        return
    skalierungsfaktor=skalierungsfaktorBerechnen()
    screen.delete("all")
    spielAktuallisieren()
    for y in range(len(spielbrett.spielfeld)):
        for x in range(len(spielbrett.spielfeld[y])):
            if spielbrett.spielfeld[y][x]==1:
                color="green" 
            else:
                color="white"
            screen.create_rectangle(x*skalierungsfaktor,
                                    y*skalierungsfaktor,
                                    (x+1)*skalierungsfaktor,
                                    (y+1)*skalierungsfaktor,
                                    fill=color,
                                    outline="gray"
                                    )
    if root.winfo_exists():
        screen.after(1000,spielbrettZeichnen)

#Ändert Bearbeitungsmodus
def bearbeitenSchalter():
    global bearbeiten
    bearbeiten=bearbeiten==False
    if bearbeiten:
        bearbeitenButton.config(fg="red")
    else:
        bearbeitenButton.config(fg="black")

#Ändert status eines Spieler beim anklicken
def statusAendern(event):
    if bearbeiten:
        skalierungsfaktor=skalierungsfaktorBerechnen()
        xClick=int(event.x//skalierungsfaktor)
        yClick=int(event.y//skalierungsfaktor)
        if 0<=xClick<textfeldBreite.get() and 0<=yClick<textfeldHoehe.get():
            if spielbrett.spielfeld[yClick][xClick]==0:
                spielbrett.spielfeld[yClick][xClick]=1
                color="green"
            elif spielbrett.spielfeld[yClick][xClick]==1:
                spielbrett.spielfeld[yClick][xClick]=0
                color="white"
            screen.create_rectangle(xClick*skalierungsfaktor,
                        yClick*skalierungsfaktor,
                        (xClick+1)*skalierungsfaktor,
                        (yClick+1)*skalierungsfaktor,
                        fill=color,
                        outline="gray"
                        )
            spielerErstellen()


#Titel
ueberschrift=tk.Label(root,text="GMGL")
ueberschrift.grid(column=0,row=0)

#Canvas erstellen
screen=tk.Canvas(root,width=canvasBreite,height=canvasHöhe,bg="white")
screen.grid(row=2,columnspan=9)
#Canvas auf Clicken reagieren lassen
screen.bind("<Button-1>",statusAendern)

#Eingabefeld für spielbrettgröße(Anzahl der spieler)
eingabeLabelHoehe=tk.Label(root,text="Höhe:")
eingabeLabelHoehe.grid(column=0,row=4)
eingabeHoehe=tk.Entry(root,width=5,textvariable=textfeldHoehe)
eingabeHoehe.grid(column=1,row=4)
eingabeLabelBreite=tk.Label(root,text="Breite:")
eingabeLabelBreite.grid(column=2,row=4)
eingabeBreite=tk.Entry(root,width=5,textvariable=textfeldBreite)
eingabeBreite.grid(column=3,row=4)

#Buttons
#Button für neues Spielbrett
neuesSpielbrettButton=tk.Button(text="Neues Spielbrett",command=neuesSpielbrett)
neuesSpielbrettButton.grid(column=4,row=4)
#Button um Spielfeld zufällig zu Beleben
zufaelligFuellenButton=tk.Button(text="Zufällig füllen",command=zufaelligFuellen)
zufaelligFuellenButton.grid(column=5,row=4)
#Button zum stoppen der Animation
stoppKnopf=tk.Button(text="Animation stoppen",command=animationAbbrechen)
stoppKnopf.grid(column=7,row=4)
#Button zum starten der Animation
startKnopf=tk.Button(text="Animation starten",command=animationStarten)
startKnopf.grid(column=8,row=4)
#Button zum bearbeiten mit der Maus
bearbeitenButton=tk.Button(text="Pinsel",command=bearbeitenSchalter)
bearbeitenButton.grid(column=6,row=4)

root.mainloop()
