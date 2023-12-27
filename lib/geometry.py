import win32gui
from time import sleep
from math import sqrt
from main import *

def rectangle(x1,x2,y1,y2,color):
    hdc = win32gui.GetDC(0)
    for x in range(x1,x2):
        for y in range(y1,y2):
            win32gui.SetPixel(hdc,x,y,color)
    win32gui.ReleaseDC(0, hdc)

def cercle(xc,yc,rc,epaisseurc,color):
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

def demi_cercle(xc,yc,rc,epaisseurc,color):
    hdc = win32gui.GetDC(0)
    for rc_epaisseur in range(rc,epaisseurc+rc):
        rc_epaisseur2=rc_epaisseur**2
        for x in range(-rc_epaisseur,rc_epaisseur):
            win32gui.SetPixel(hdc,xc+x,int(sqrt(rc_epaisseur2-x**2))+yc,color)
    win32gui.ReleaseDC(0, hdc)

sourire_color = 0x00FF00

def set_sourire_on_screen(color=sourire_color):
    global sourire_color
    sourire_color = color
    try:
        cercle(800,400,120,15,sourire_color)
        cercle(750,360,5,10,sourire_color)
        cercle(850,360,5,10,sourire_color)
        demi_cercle(800,410,70,5,sourire_color)
        log("Sucessfuly set_sourire_on_screen")
    except Exception as E:
        log(f"Error {E} while trying to set_sourire_on_screen")