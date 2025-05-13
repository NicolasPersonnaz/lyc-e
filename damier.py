from turtle import *
speed(100)
def bouge(x,y) :
    up()
    goto(x,y)
    down()
def carre(couleur) :
    begin_fill()
    fillcolor(couleur)
    for i in range(4) :
        down()
        fd(40)
        left(90)
    fd(40)
    end_fill()
def ligne(j):
    up()
    x = -200
    y = 200
    for i in range(10):
        if (i+j)%2 == 0 :

            carre("black")
        else :

            carre("white")

        x = x + 40

def damier():
    up()
    y = 200
    x = -200
    goto(x,y)
    for j in range(10):
        ligne(j)
        up()
        y = y - 40
        goto(x,y)
        down()


damier()



