from turtle import*
import random
title("jugando ando")
bgcolor("black")
pencolor("white")

left(30)  
def dibujar_triangulo(longitud):
    for i in range(3):
        left(120)
        forward(longitud)

def dibujar_hexagono(longitud):
    speed(0)
    for i in range(6):
        left(60)
        dibujar_triangulo(longitud)

for i in range (9):
    dibujar_hexagono(300+i*2)
    right(3)
mainloop()

"""
def dibujar_cuadrado(longitud):
    for i in range(5):
        left(90)
        forward(longitud)
speed(0)
dibujar_cuadrado(200)
left(135)
forward(282.84)
backward(141.42)
left(90)
forward(141.42)
backward(141.42)
left(45)
forward(100)
left(135)
forward(70)
right(135)
forward(50)
mainloop()
"""