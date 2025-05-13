from turtle import *
def koch(c) :
    pendown
    forward(c)
    left(60)
    forward(c)
    right(120)
    forward(c)
    left(60)
    forward(c)
    exitonclick()
koch(100)



def koch_recurs(c,n) :

    if n == 0 :
        forward(c)
    else :

        koch_recurs(c,n-1)
        left(60)
        koch_recurs(c,n-1)
        right(120)
        koch_recurs(c,n-1)
        left(60)
        koch_recurs(c,n-1)
penup()
goto(-100,-100)
pendown()
print(koch_recurs(5,4))
exitonclick()


