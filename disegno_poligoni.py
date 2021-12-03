#dato un numero in input disegnare un poligono con n lati
import turtle

tar = turtle.Turtle()
tar.hideturtle()
lati = int(input("inserisci il numero dei lati: "))
gradi = (180*(lati-2))/lati
temp = gradi-90
print(gradi)
schermo = turtle.getscreen()
for _ in range(lati):
    tar.forward(100)
    tar.left(90-temp)

turtle.exitonclick()