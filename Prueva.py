import turtle
class Triangulo(object):
    
    primer_punto = [None, None]
    segundo_punto =[None,  None]
    tercer_punto = [None, None]
    t = None
    def __init__(self, primero, segundo, tercero, pluma):
        self.primer_punto = primero
        self.segundo_punto = segundo
        self.tercer_punto = tercero
        self.t = pluma

    def imprimir_coordindas(self):
        print('El triangulo tiene tres puntos en estas  coordinadas')
        print(str(self.primer_punto) + str(self.segundo_punto) + str(self.tercer_punto))
    
    def cambiar_coordinadas(self, punto, nuevas_coordinadas):
        if punto > 3 or punto < 1:
            return None
        if punto == 1:
            self.primer_punto = nuevas_coordinadas
        elif punto == 2:
            self.segundo_punto = nuevas_coordinadas
        elif punto == 3:
            self.tercer_punto = nuevas_coordinadas

    def dibujar_triangulo(self):
        self.t.pencolor('white')
        self.t.goto(self.primer_punto[0], self.primer_punto[1])
        self.t.goto(self.segundo_punto[0], self.segundo_punto[1])
        self.t.goto(self.tercer_punto[0], self.tercer_punto[1])
    
    def mover_derecha(self, pixeles):
        self.primer_punto
        self.segundo_punto
        self.tercer_punto
        a.cambiar_coordinadas(2, [-300,0])
        return True

    def mover_izquierda(self, pixeles):
        self.primer_punto
        self.segundo_punto
        self.tercer_punto
        a.cambiar_coordinadas(1, [0,-300])
        return True
    
    def mover_arriba(self, pixeles):
        self.primer_punto
        self.segundo_punto
        self.tercer_punto
        a.cambiar_coordinadas(1, [300,0])
        return True

    def mover_abajo(self, pixeles):
        self.primer_punto
        self.segundo_punto
        self.tercer_punto
        a.cambiar_coordinadas(3, [0,-300])
        return True



pluma = turtle.Pen()
turtle.bgcolor('black')

a = Triangulo([0,0], [300,0], [0,300], pluma)

a.imprimir_coordindas()
a.dibujar_triangulo()
a.mover_derecha(200)
a.imprimir_coordindas()
a.dibujar_triangulo()
a.mover_izquierda(200)
a.imprimir_coordindas()
a.dibujar_triangulo()
a.mover_abajo(200)
a.imprimir_coordindas()
a.dibujar_triangulo()
a.mover_arriba(200)
a.imprimir_coordindas()
a.dibujar_triangulo()

turtle.exitonclick()