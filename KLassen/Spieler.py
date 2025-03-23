#Milan

from tkinter import *

class Spieler:
    def __init__(self,x,y,status):
        self.x=x
        self.y=y
        self.status=status
        self.umgebung=[[0,0,0],[0,0,0],[0,0,0]]

    def umgebungAktuallisieren(self,spielbrett):
        for dy in range(-1,2):
            for dx in range(-1,2):
                ny,nx=self.y+dy,self.x+dx
                if 0 <= ny < len(spielbrett) and 0 <= nx < len(spielbrett[0]):
                    self.umgebung[dy+1][dx+1]=spielbrett[ny][nx]
                else:
                    self.umgebung[dy+1][dx+1]=0  #Randzellen als tot setzen

    def umgebungAnalysieren(self):
        anzahlLebendigerSpieler=0
        for i in range(3):
            for j in range(3):
                if (i,j) != (1,1) and self.umgebung[i][j]:  #Sich selbst ignorieren
                    anzahlLebendigerSpieler += 1
        return anzahlLebendigerSpieler

    def update(self,spielbrett):
        self.umgebungAktuallisieren(spielbrett)
        lebendigeSpieler=self.umgebungAnalysieren()

        if lebendigeSpieler >= 4 or lebendigeSpieler <= 1:
            self.status=0  #Stirbt an Überbevölkerung oder Einsamkeit
        elif lebendigeSpieler == 3:
            self.status=1  #Wird geboren oder bleibt am Leben
