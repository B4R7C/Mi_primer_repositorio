#TUTORIAL #1 CREAR UNA VENTANA EN PYGAME "HOLA MUNDO" #1
#inicializar pygame, sys nos ayuda a poder serrar nuestra ventana #1
import pygame,sys
from pygame import color 

#importar todos sus modulos #1
from pygame. locals import *

#lo utilizamos para crar una ventana del juego y sus dimenciones en este caso 400,300 #1
ventana = pygame.display.set_mode((400,300))

#TUTORIAL #2 USO Y CREACION DE COLORES
#colores primarios, pygame usa el sistema rgb, este parametro usa colores del 0 al 255, vamos a definir un color 
#rojo,verde,azul
#RGB(120, 50, 50)
#nuevo color metodo #1
#Color = (0,140,60)
# #nuevo color #2
#ColorDos = pygame.color(255,120,9)
#ESTO SE DEFINE DESPUES DE IMPORTAR PYGAME
#AQUI DEFINIMOS EL COLOR #2
Color = pygame.Color(200,0,0)

# antes de hacer uso de cualquiermodulo tenemos que inicializarlos #1
pygame.init()

#agregar un mensaje a la ventana
pygame.display.set_caption("hola mundo")

#TUTORIAL #3 PROFUNDIZACION DE LOS COLORES Y CREACION DE LINEAS PARA CREAR POLIGONOS, COMO ESTA CONFORMADA NUESTRA VENTANA 
#Para poder movernos en nuestra ventana necesitamos cordenadas, con las cuales usamos un plano cartesiano (x, y) dentro de este plano y estas cordenadas hay pixeles 
#las cordenadas funcionan igual que en turtle 
#EJEMPLO SE ENCUENTRA DEBAJO DE LA DEFINICION DEL COLOR (VAMOS A DIBUJAR UNA LINEA ESTO SE ENCUENTRA ARRIBA)
#AQUI VAMOS A DIBUJAR UNA FIGURA #3
#Para esto necesitamos tres parametros 
#1.Una superficie = ventana 
#2.El color de la linea = Color 
#3.Punto inicial en x,y de la linea = (cordenadas o tupla) = (60,80)
#!.En el caso del rectangulo o rect en el 3er parametro no se define el punto inicial, si no que es una tupla de cuatro valores, los primero dos valores refieren a la esquina izquierda superior de nuestro rectangulo, el tercer valor de la tupla es el ancho del rectangulo y el cuarto valor es lo alto 
#!.En el caso del poligono se describen todas sus partes en una tupla dento de una tupla
#4.Punto final en x,y de la linea = (cordenadas o tupla) = (160,100)
#!.En caso del circulo o circle en el 4to parametro no se define el punto final, si no que el radio
#5.El ancho de nuestra linea o figura en pixeles 
#ESTO QUEDARIA ASI 

pygame.draw.line(ventana,Color,(60,80),(160,100),5)

#TUTORIAL #4 DIBUJAR DIFERENTES POLIGONOS Y FIGURAS GEOMETRICAS
#para definir que se va a dibujar usabamos pygame.draw.nombre de la figura

pygame.draw.circle(ventana,(8,70,120),(80,90),20)
pygame.draw.rect(ventana,Color,(0,0,100,50))
pygame.draw.polygon(ventana,Color,((80,90),(150,100),(40,80),(60,80)))

#TUTORIAL #5 cargar imagenes en pygame
#vamos a cargr una imagen con el comando pygame.image.load en este vamos a describir la direccion de nuestra imagen 
#Mi_imagen = pygame.image.load("Imagenes/Descargas/Imagenes/Niankat.png")
#ahora describimos las cordenadas en las que va a estar nuestra imagen hay 2 formas
#Forma 1
PosX,posY = 130,128
#Forma 2
#posX = 130
#posY = 70
#la imagen tambien tiene parametros 
#1.poner la imagen en las ventanas con ventana.blit
#2.poner la direccion de la imagen ya antes definida en este caso (Mi_imagen)
#3.ponemos la posicion en x y en y previamente definidas (PosX,PosY)
#4. como la imagen esta descrita en una figura, sea un cualquier figura, tenemos que poner las mismas cordenadas, casi siempre un rectangulo, en el cual definimos sus dos esquinas como lo hicimos anteriormente
#ventana.blit(Mi_imagen),(PosX,posY)

#Para saber la cantidad de saturacion que tiene un color en nuestro pixel usamos: #3
print (Color.r) #r de red
print (Color.g) #g de green 
print (Color.b) #b de blue

#con un loop infinito recorremos la lista de eventos de pygame, en este caso para serrar la ventana #1
while True:
    #darle color a nuestra ventana 
    #ventana.fill()
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit() 

    pygame.display.update()
#!corre el codigo¡


