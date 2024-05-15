import random

def GenerarValorCartas():
    card_values = {
        'caballo': 10,
        'rey': 10,
        'sota': 10,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10
    }
    return random.sample(list(card_values.values()), k=4)

def calcularpuntos(mano):
    puntos = sum(mano)
    return puntos

CartasJugador1 = GenerarValorCartas()
CartasJugador2 = GenerarValorCartas()

Figuras = [10, 10, 10]
lowest_value = 1

PuntosJugador1 = calcularpuntos(CartasJugador1)
PuntosJugador2 = calcularpuntos(CartasJugador2)

ManoJugador1 = ""
ManoJugador2 = ""

if max(CartasJugador1) in Figuras and min(CartasJugador1) in Figuras:
    ManoJugador1 = "Jugada Grande"
elif len(set(CartasJugador1)) == 2:
    ManoJugador1 = "Jugada Doble"
elif min(CartasJugador1) == lowest_value:
    ManoJugador1 = "Jugada Pequeña"
else:
    ManoJugador1 = "Jugada Media"
    


if max(CartasJugador2) in Figuras and min(CartasJugador2) in Figuras:
    ManoJugador2 = "Jugada Grande"
elif len(set(CartasJugador2)) == 2:
    ManoJugador2 = "Jugada Doble"
elif min(CartasJugador2) == lowest_value:
    ManoJugador2 = "Jugada Pequeña"
else:
    ManoJugador2 = "Jugada Media"

if PuntosJugador1 >= 40:
    print("El jugador 1 gana con 40 o mas puntos!")
elif PuntosJugador2 >= 40:
    print("El jugador 2 gana con 40 o mas puntos!")
else:
    print("Ambos jugadores no llegaron a los 40 puntos")
