import random
def regresar_indices(numero):
    if numero > 9 or numero < 1:
        print("Tu numero es invalido")
        return None 
    if numero <= 3:
        return [0,numero-1]
    if numero <= 6:
        return [1, numero-4]
    elif numero <= 9:
        return [2, numero-7]

tictactoe = [[1,2,3],[4,5,6,],[7,8,9]]

def imprimir_ttt(tictactoe):
    print (tictactoe [0])
    print (tictactoe [1])
    print (tictactoe [2])

def check(numero):
    indices = regresar_indices(numero)
    if type(tictactoe[indices[0]][indices[1]]) == type('x'):
        print('Este espacio esta ocupado')
        return False 
    if type(tictactoe[indices[0]][indices[1]]) == type(1):
        print('Este espacio esta libre')
        return True 

def checar_estado_de_juego(ttt):
    for fila in ttt:
        if fila in ttt:
            if fila.count(emoji_elegido) == 3:
                return 1
            if fila.count(emoji_elegido2) == 3:
                return 2
    
    for i in range(3):
        if (ttt[0][i] == ttt[1][i] == ttt[2][i]):
            if ttt[0][i] == emoji_elegido:
                return 1
            elif ttt[0][i] == emoji_elegido2:
                return 2 

    if (ttt[0][0] == ttt[1][1] and ttt[1][1]== ttt[2][2]):
        if ttt[0][0] == emoji_elegido:
            return 1
        elif ttt[0][0] == emoji_elegido2:
            return 2 
    if (ttt[0][2] == ttt[1][1] and ttt[1][1] == ttt[2][0]):
        if ttt[0][2] == emoji_elegido:
            return 1
        elif ttt[0][2] == emoji_elegido2:
            return 2 
    return 0


def jugar_computadora(ttt):
    emoji_compu = "🤖"
    #generar un numero aleatorio de 1-9
    lugar_aleatorio = random.randint(1,9)
    while(check(lugar_aleatorio)== False):
        lugar_aleatorio = random.randint(1,9)
    #hay un lugar disponible 
    indices = regresar_indices(lugar_aleatorio)
    ttt[indices[0]][indices[1]] = emoji_compu

la_partida_sigue = True 

print("BIENVENIDOS A TIC TAC TOE ")
imprimir_ttt(tictactoe)

respondio_bien = False 
Oponente_computadora = False 
while(respondio_bien == False):
    jugar_compu = input("Quieres jugar cotra la computadora si/no: ")
    if jugar_compu =="si":
        Oponente_computadora = True 
        respondio_bien = True 
    elif jugar_compu == "no":
        Oponente_computadora = False
        respondio_bien = True 
    else:
        print("Tu respuesta no es valida. Intentalo de nuevo")

lugares = 9
escogio_su_emoji_bien = False 
print("escoge tu emoji jugador 1: 1.👾 2.👻 3.👽 4.✨ 5.🙈 6.🌈 7.🕴️  8.🫧  9.🫀  10.🐤")
lista_de_emojis = ["👾", "👻", "👽", "✨","🙈", "🌈","🕴️", "🫧","🫀","🐤"]
while not escogio_su_emoji_bien:
    emoji_jug1 = int(input("porfavor elija su emoji: "))
    escogio_su_emoji_bien = False 

    if emoji_jug1 >= 1 and emoji_jug1 <= 10:
        emoji_elegido = lista_de_emojis[emoji_jug1-1]
        print (emoji_elegido)
        escogio_su_emoji_bien = True
        
    else:
        print("elija un valor valido")
        escogio_su_emoji_bien = False 

if Oponente_computadora == False:
    escogio_su_emoji_bien = False 
    print("escoge tu emoji jugador 2: 1.👾 2.👻 3.👽 4.✨ 5.🙈 6.🌈 7.🕴️ 8.🫧 9.🫀 10.🐤")
    while not escogio_su_emoji_bien:
        emoji_jug2 = int(input("porfavor elija su emoji: "))
        escogio_su_emoji_bien = False 

        if emoji_jug2 >= 1 and emoji_jug1 <= 10:
            emoji_elegido2 = lista_de_emojis[emoji_jug2-1]
            print (emoji_elegido2)
            escogio_su_emoji_bien = True
            
            if emoji_elegido2 == emoji_elegido: 
                print("el jugador 1 ya eligio este emoji, elige otro")
                escogio_su_emoji_bien = False 

        
            else:
                print("Escogio su emoji bien")
                escogio_su_emoji_bien = True
else:
    emoji_elegido2 = "🤖"

while(la_partida_sigue):
    if lugares <= 0:
        la_partida_sigue = False 
    print("turno del jugador 1")
    input_valido = False 
    while (input_valido == False):
        lugar = int(input(f"ingresa el lugar donde quieres poner tu {emoji_elegido}: "))
        input_valido = check(lugar)
        if input_valido == False:
            print('Has ingresado un lugar invalido, intentalo de nuevo')
    indices = regresar_indices(lugar)
    tictactoe [indices[0]][indices[1]] = emoji_elegido
    estado = checar_estado_de_juego(tictactoe)
    imprimir_ttt(tictactoe)
    if estado == 1 or estado == 2:
        la_partida_sigue = False 
        print(f'ha ganado el jugador {estado}')
        break
    lugares -= 1
    if lugares <= 0:
        la_partida_sigue = False 
        print('Ya no hay lugares empataron')
        break

    if Oponente_computadora == False:
        print ("Turno del jugador 2")
        input_valido = False 
        while (input_valido == False):
            lugar = int(input(f"ingresa el lugar donde quieres poner tu {emoji_elegido2}: "))
            input_valido = check(lugar)
            if input_valido == False:
                print('Has ingresado in lugar invalido, intentalo de nuevo')
        indices = regresar_indices(lugar)
        tictactoe [indices[0]][indices[1]] = emoji_elegido2
        estado = checar_estado_de_juego(tictactoe)
        imprimir_ttt(tictactoe)
        if estado == 1 or estado == 2:
            la_partida_sigue = False 
            print(f'ha ganado el jugador {estado}')
            break
        lugares -= 1
        if lugares <= 0: 
            la_partida_sigue = False 
            print('Ya no hay lugares, empataron')
            break 
    else:
        jugar_computadora(tictactoe)
        estado = checar_estado_de_juego(tictactoe)
        imprimir_ttt(tictactoe)
        if estado == 1 or estado == 2:
            la_partida_sigue = False 
            print(f'ha ganado el jugador {estado}')
            break
