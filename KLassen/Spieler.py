#Milan

from tkinter import *

class Spieler:
    def __init__(self,x,y,status):
        self.x=x
        self.y=y
        self.status=status
        self.umgebung=[[0,0,0],[0,0,0],[0,0,0]]

    def umgebungAktuallisieren(self,spielbrett):
        for y in range(-1,2):
            for x in range(-1,2):
                ny=self.y+y
                nx=self.x+x
                if 0<=ny<len(spielbrett) and 0<=nx<len(spielbrett[0]):
                    self.umgebung[y+1][x+1]=spielbrett[ny][nx]
                else:
                    self.umgebung[y+1][x+1]=0

    def umgebungAnalysieren(self):
        anzahlLebendigerSpieler=0
        for i in range(0,3):
            for j in range(0,3):
                if (i,j)!=(1,1) and self.umgebung[i][j]==1:
                    anzahlLebendigerSpieler+=1
        return anzahlLebendigerSpieler

    def update(self,spielbrett):
        self.umgebungAktuallisieren(spielbrett)
        lebendigeSpieler=self.umgebungAnalysieren()

        if lebendigeSpieler>=4 or lebendigeSpieler<=1:
            self.status=0
        elif lebendigeSpieler==3:
            self.status=1
