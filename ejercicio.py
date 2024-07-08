def elegir_emojis():
    lista_de_emojis = ["👾", "👻", "👽", "✨","🙈", "🌈","🕴️", "🫧","🫀","🐤"]
    mensaje = "Escoge tu emoji: 1.👾, 2.👻, 3.👽, 4✨, 5.🙈, 6.🌈, 9.🕴️, 10.🫧, 11.🫀, 12.🐤"

    indice_jugador1 = None 
    indice_jugador2 = None 
    emoji_jugador1 = None 
    emoji_jugador2 = None 
    
    escogio_bien_su_indice = False 
    print("Para el jugador 1: ")
    while (escogio_bien_su_indice == False):
        indice_jugador1 = int(input(mensaje))
        if indice_jugador1 >=1 and indice_jugador1 <= 10:
            print("tu indice es correcto")
            emoji_jugador1 = lista_de_emojis[indice_jugador1-1]
            escogio_bien_su_indice = True 
        
        else:
            print("Tu indice es correcto, intentalo otra vez")
