from mlibreria import *

if __name__ == '__main__':
    pg.init()
    pantalla = pg.display
    pg.display.set_mode((ANCHOVENTANA,ALTOVENTANA))

    fin = False
    while not fin:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                fin = True