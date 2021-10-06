import pygame
from pygame import time
from pygame.display import set_mode
from mlibreria import *

if __name__ == '__main__':
    pg.init()
    pantalla = pg.display.set_mode((ANCHOVENTANA,ALTOVENTANA))
    PonerPunto(pantalla, [30,80], color= SALMON)
    reloj = pg.time.Clock()
    angle = 0
    fin = False
    while not fin:
        pantalla.fill(BLACK)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                fin = True
        punto = rotarPuntosGradosHorario([[30,80]], angle)[0]
        PonerPunto(pantalla, punto, color = SALMON)
        angle += 1
        reloj.tick(60)

                
                