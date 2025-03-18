#Milan

import random
from tkinter import *

class Spieler:
    def __init__(self,x,y,status):
        self.x=x
        self.y=y
        self.status=status
        self.umgebung=[[0,0,0],[0,0,0],[0,0,0]]
    def umgebungAktuallisieren(self, spielbrett):
        self.umgebung[0][0]=spielbrett[self.y-1][self.x-1]
        self.umgebung[0][1]=spielbrett[self.y-1][self.x]
        self.umgebung[0][2]=spielbrett[self.y-1][self.x+1]
        self.umgebung[1][0]=spielbrett[self.y][self.x-1]
        self.umgebung[1][1]=spielbrett[self.y][self.x]
        self.umgebung[1][2]=spielbrett[self.y][self.x+1]
        self.umgebung[2][0]=spielbrett[self.y+1][self.x-1]
        self.umgebung[2][1]=spielbrett[self.y+1][self.x]
        self.umgebung[2][2]=spielbrett[self.y+1][self.x+1]

    def umgebungAnalysieren(self):
        anzahlLebendigerSpieler=0
        for i in self.umgebung:
            for j in range(0,3,1):
                if self.umgebung[i][j]:
                    anzahlLebendigerSpieler+=1
        return anzahlLebendigerSpieler
    def update(self):
        self.umgebungAktuallisieren()
        lebendigeSpieler=self.umgebungAnalysieren()
        if lebendigeSpieler>=4 or lebendigeSpieler<=2:
            self.status=0
        elif lebendigeSpieler==3:
            self.status=1
        