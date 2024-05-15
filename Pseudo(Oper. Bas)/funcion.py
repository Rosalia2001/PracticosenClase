import random

def bucle(j1, j2, j3, j4):
    while True:
        c1 = random.randint(1, 13)
        print("El jugador 1 dice ", j1)
        print("jugador 1 tira la carta", c1)
        c2 = random.randint(1, 13)
        print("El jugador 2 dice ", j2)
        print("jugador 2 tira la carta", c2)
        c3 = random.randint(1, 13)
        print("El jugador 3 dice ", j3)
        print("jugador 3 tira la carta", c3)
        c4 = random.randint(1, 13)
        print("El jugador 4 dice ", j4)
        print("jugador 4 tira la carta", c4)
        if ((c1 == j1) or (c2 == j2) or (c3 == j3) or (c4 == j4)):
            break
    print("Como dos cartas son iguales, entonces elegiremos al ganador ")
    cj1 = random.randint(1, 4)
    cj2 = random.randint(1, 4)
    cj3 = random.randint(1, 4)
    cj4 = random.randint(1, 4)
    return cj1, cj2, cj3, cj4

def ganador(cj1, cj2, cj3, cj4):
    if (cj1 == 4):
        return f"El ganador es el jugador {c}"
    elif (cj2 == 4):
        return f"El ganador es el jugador {c}"
    elif (cj3 == 4):
        return f"El ganador es el jugador {c}"
    elif (cj4 == 4):
        return f"El ganador es el jugador {c}"
    else:
        return "No hay ganador"