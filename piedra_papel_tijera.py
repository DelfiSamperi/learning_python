import random

def game():
    user = input("Elije una opción: 'piedra', 'tijera' o 'papel':\n").lower()
    computer = random.choice(['piedra', 'papel', 'tijera'])
    print(f"La computadora eligió {computer}")

    if user == computer:
        return 'Empate'
    
    if ganó_el_jugador(user, computer):
        return 'Ganaste!!'
    
    return 'Perdiste...  :('


def ganó_el_jugador(jugador, oponente):
    # retorna true si gana el jugador
    # piedra gana tijera (pi > ti)
    # tijera gana papel (ti > pa)
    # papel gana piedra (pa > pi)
    if ((jugador == 'piedra' and oponente == 'tijera')
        or (jugador == 'tijera' and oponente == 'papel')
        or (jugador == 'papel' and oponente == 'piedra')):
        return True
    else:
        return False
    

print(game())


