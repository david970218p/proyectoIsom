import pygame
from pygame import time
from pygame.display import set_mode
from pygame.draw import line
from mlibreria import *

if __name__ == '__main__':
    pg.init()
    pantalla = pg.display.set_mode((ANCHOVENTANA,ALTOVENTANA))
    PonerPunto(pantalla, [30,80], color = SALMON)
    PonerPunto(pantalla, [30,80], color = RED)
    reloj = pg.time.Clock()
    angle = 0
    fin = False
    while not fin:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                fin = True
        punto = rotarPuntosGradosHorario([[80,80]], angle)[0]
        punto2 = rotarPuntosGradosHorario([[0,0]], angle , punto)[0]
        punto3 = rotarPuntosGradosHorario([[0,0]], angle, punto2)[0]
        PonerPunto(pantalla, punto, color = SALMON)
        PonerPunto(pantalla, punto2)
        PonerPunto(pantalla, punto3, color = GREEN)
        ls = trasladarPuntos([punto,punto2,punto3], CENTRO)
        dibujarTriangulo(pantalla, ls, PURPLE)
        angle += 1
        reloj.tick(60)

                
                