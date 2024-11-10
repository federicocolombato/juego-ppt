nombre1 = input("¿Como se llamara el jugador 1? ")
nombre2 = input("¿Como se llamara el jugador 2? ")

puntosj1 = 0
puntosj2 = 0
partidas = 0

while partidas < 3:

    jugador1 = input("Hola " + nombre1 + "¿Qué eliges? ¿Piedra, Pale o Tijeras?: ").lower()
    jugador2 = input("Hola " + nombre2 + "¿Qué eliges? ¿Piedra, Pale o Tijeras?: ").lower()

    condision1 = jugador1 == "piedra" and jugador2 == "tijeras"
    condicion2 = jugador1 == "tijeras" and jugador2 == "papel"
    condicion3 = jugador1 == "papel" and jugador2 == "piedra"

    if jugador1 == jugador2:
        print("Ha sido un empate")
    elif condision1 or condicion2 or condicion3:
         print("Ha ganado", nombre1)
         puntosj1 += 1
    else:
        print("Ha ganado", nombre2)
        puntosj2 += 1
    
    partidas += 1

if puntosj1 > puntosj2:
    puntosj1 = str(puntosj1)
    print("El ganador del partido fue: " + nombre1 + " con: " + puntosj1 + " puntos")
elif puntosj2 > puntosj1:
    puntosj2 = str(puntosj2)
    print("El ganador del partido fue: " + nombre2 + " con: " + puntosj2 + " puntos")
else:
    print("Fue un empate")