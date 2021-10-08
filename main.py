from mlibreria import *

if __name__ == '__main__':
    pg.init()
    pantalla = pg.display.set_mode((ANCHOVENTANA,ALTOVENTANA))
    mul = 60
    a = [3 * mul,0]
    b = [2 * mul,0]
    c = [1 * mul,0]
    d = [1 * mul,0]
    e = [2 * mul,0]
    
    a_r = rotarPuntoGradosHorario(a, 30)
    a_c = CartesianoAPantalla(a_r)

    b_r = rotarPuntoGradosHorario(b, 90)
    b_c = CartesianoAPantalla(b_r, a_c)

    c_r = rotarPuntoGradosHorario(c, 210)
    c_c = CartesianoAPantalla(c_r, b_c)

    d_r = rotarPuntoGradosHorario(d, 270)
    d_c = CartesianoAPantalla(d_r, c_c)

    e_r = rotarPuntoGradosHorario(e, 210)
    e_c = CartesianoAPantalla(e_r, d_c)

    ls = [CENTRO, a_c, b_c, c_c, d_c, e_c]
    pg.draw.lines(pantalla,SALMON, True, ls)
    pg.display.flip()



    fin = False
    while not fin:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                fin = True