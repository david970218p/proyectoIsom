import pygame as pg
import math as m

ALTOVENTANA = 800
ANCHOVENTANA = 1200
CENTRO = (ANCHOVENTANA/2, ALTOVENTANA/2)

BLACK = (0,0,0)
RED = (255, 0, 0)
BLUE =(0, 0, 250)
GREEN =(0,255,0)
SALMON = (250,128,114)
PURPLE = (128,0,128)
YELLOW = (255, 255, 0)


def planoCartesiano(pantalla, centro = CENTRO, color = GREEN):
    pg.draw.line(pantalla, color, (0, centro[1]), (ANCHOVENTANA, centro[1]))
    pg.draw.line(pantalla, color, (centro[0], 0), (centro[0], ALTOVENTANA))
    pg.display.flip()

def PonerPunto(pantalla,punto, centro = CENTRO,  color = RED):
    pg.draw.circle(pantalla, color,(centro[0] + punto[0], centro[1] - punto[1]), 3)
    pg.display.flip()

def transformarPuntos(puntos, centro = CENTRO):
    lista = []
    for punto in puntos:
      nuevopunto = (centro[0] + punto[0], centro[1] - punto[1])
      lista.append(nuevopunto)
    return lista


def CartesianoAPantalla(punto, centro = CENTRO):
    return [centro[0] + punto[0], centro[1] - punto[1]]


def dibujarTriangulo(pantalla, puntos, color = SALMON):
    pg.draw.lines(pantalla, color, True, puntos)
    pg.display.flip()

def escalarPunto(punto,s):
    xp = punto[0] * s[0]
    yp = punto[1] * s[1]
    return [xp,yp]

def escalarPuntos(puntos, s, puntoFijo = None):
    if puntoFijo != None:
        pf = [-1*p for p in puntoFijo]
        puntos = trasladarPuntos(puntos, pf)
    ls = [escalarPunto(punto, s) for punto in puntos]
    if puntoFijo != None:
        ls = trasladarPuntos(ls, puntoFijo)
    return ls


def trasladarPunto(punto, t):
    xp = punto[0] + t[0]
    yp = punto[1] + t[1]
    return [xp,yp]

def trasladarPuntos(puntos, t):
    return [trasladarPunto(punto,t) for punto in puntos]

def rotarPuntoGradosHorario(punto, a_grad):
    a_rad = m.radians(a_grad)
    xp = punto[0] * m.cos(a_rad) - punto[1] *m.sin(a_rad)
    yp = punto[0] * m.sin(a_rad) + punto[1] *m.cos(a_rad)
    return[xp,yp]

def rotarPuntosGradosHorario(puntos, a_grad, puntoFijo = None):
    if puntoFijo != None:
        pf = [-1*p for p in puntoFijo]
        puntos = trasladarPuntos(puntos, pf)
    ls = [rotarPuntoGradosHorario(punto, a_grad) for punto in puntos]
    if puntoFijo != None:
        ls = trasladarPuntos(ls, puntoFijo)
    return ls


 