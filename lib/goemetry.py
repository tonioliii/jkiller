import win32gui
from time import sleep
from math import sqrt

def rectangle(x1,x2,y1,y2):
    hdc = win32gui.GetDC(0)
    for x in range(x1,x2):
        for y in range(y1,y2):
            win32gui.SetPixel(hdc,x,y,color)
    win32gui.ReleaseDC(0, hdc)

def cercle(xc,yc,rc,epaisseurc):
    hdc = win32gui.GetDC(0)
    for rc_epaisseur in range(rc,epaisseurc+rc):
        rc_epaisseur2=rc_epaisseur**2
        for x in range(-rc_epaisseur,rc_epaisseur):
            win32gui.SetPixel(hdc,xc+x,-int(sqrt(rc_epaisseur2-x**2))+yc,color)
        for x in range(-rc_epaisseur,rc_epaisseur):
            win32gui.SetPixel(hdc,xc+x,int(sqrt(rc_epaisseur2-x**2))+yc,color)
        for y in range(-rc_epaisseur,rc_epaisseur):
            win32gui.SetPixel(hdc,-int(sqrt(rc_epaisseur2-y**2))+xc,yc+y,color)
        for y in range(-rc_epaisseur,rc_epaisseur):
            win32gui.SetPixel(hdc,int(sqrt(rc_epaisseur2-y**2))+xc,yc+y,color)
    win32gui.ReleaseDC(0, hdc)

def demi_cercle(xc,yc,rc,epaisseurc):
    hdc = win32gui.GetDC(0)
    for rc_epaisseur in range(rc,epaisseurc+rc):
        rc_epaisseur2=rc_epaisseur**2
        for x in range(-rc_epaisseur,rc_epaisseur):
            win32gui.SetPixel(hdc,xc+x,int(sqrt(rc_epaisseur2-x**2))+yc,color)
    win32gui.ReleaseDC(0, hdc)

color = 0x00FF00

def sourire():
    cercle(800,400,120,15)
    cercle(750,360,5,10)
    cercle(850,360,5,10)
    demi_cercle(800,410,70,5)
