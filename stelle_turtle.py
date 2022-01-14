import turtle
import random
DIM_SCHERMO = 400

def stella(x,y,tr): #stella con cordinate random
    tr.up()
    tr.goto(x,y)
    tr.down()
    for _ in range(5):
        tr.forward(250)
        tr.right(144)

def stelleRandom(tr):   
    for _ in range(50):
        tr.up()
        tr.goto(random.uniform(-DIM_SCHERMO,DIM_SCHERMO),random.uniform(-DIM_SCHERMO,DIM_SCHERMO))
        tr.down()
        for _ in range(5):
            tr.forward(100)
            tr.right(144)

tr = turtle.Turtle()
schermo = turtle.getscreen()
turtle.screensize(canvwidth=DIM_SCHERMO, canvheight=DIM_SCHERMO)
x = int(input("inserisci la cordinata X: "))
y = int(input("inserisci la cordinata Y: "))

stella(x,y,tr)
stelleRandom(tr)

turtle.exitonclick()