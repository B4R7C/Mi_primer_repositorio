#FUNCIONES IMPORTANTES DE TURTLE
#importamos el paquete "turtle"
import turtle
#inicializamos la pluma de turtle
t = turtle.Pen()
#definimos el color de la pluma, hexcolor
t.pencolor("blue")
#definimos la anchura de la pluma 
t.width(10)
#mandamos a turtle dibujar una linea recta con una longitud, en pixeles. en este caso son 100 pixeles
t.forward(100)
#mandamos que la pluma se dirija a la derecha en un angulo proveido, en este caso, 90 grados a la derecha 
t.left(90)
t.forward(100)
#lo mismo que arriba, pero a la izquierda
t.left(90)
t.forward(100)
#definir velocidaad de la pluma
t.speed(3)
#el color de fondo 
turtle.bgcolor("grey")

#FUNCIONES QUE SE PUEDEN USAR APARTE
#alzamos la pluma, osea, no dibujamos cuando nos movemos 
t.penup

#para que no se sierre turtle
turtle.exitonclick()

#BUCLE DE TURTLE
for i in range ()
input("preciona cualquier tecla para terminar")



