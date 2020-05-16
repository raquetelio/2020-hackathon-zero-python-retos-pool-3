from random import randint

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'

def quienGana(p_player, p_ai):
    resultados = ['Empate!', 'Ganaste!', 'Perdiste!']
    player = p_player.lower
    ai = p_ai.lower
    
    if player == ai:
        resultado = resultados[0] # Empate
    elif (player == options[0] and ai == options[2]) or (player == options[2] and ai == options[1]) or (player == options[1] and ai == options[0]):
            resultado = resultados[1] # Jugador gana # Si es Piedra + Tijeras , Tijeras + Papel o Papel + Piedra
    else: 
        resultado = resultados[2] # Jugador pierde

    return resultado

# Entry Point
def Game():
    #
    #
    while player not in options:
        player = input("Escoge una acción [Piedra - Papel - Tijera]")

    #
    #
    aleatorio = randint(0,2)
    ai = options[i]

    print("..." + ai)
    winner = quienGana(player, ai)

    print(winner)

