import random
tablero = [[]]
t = random.randint(1, 10) #numero de juegos a jugar
n = random.randint(2, 2000) #tamaño del tablero
r1 = random.randint(1, n) #fila de las torres del jugador 1
r2 = random.randint(1, n) #fila de las torres del jugador 2

#creacion del tablero
def creacion_tablero(n):
    r1
    r2
    i = n
    j = n
    print(n)
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            tablero[i] = tablero[r1]
            tablero[r1][j] = "T1"
            tablero[i] = tablero[r2] = "T2"
            tablero[r2][j] = "T2"
    return tablero

# funcion gana jugador 1
def gana_jugador_uno():
    if r1 == r2 - 1 and r2 == n:
        return True
    elif r2 == r1 - 1 and r1 == n:
        return False
    elif r1 == r2 + 1 and r2 == 0:
        return True
    elif r2 == r1 + 1 and r1 == 0:
        return False





#codigo principal
n = random.randint(2, 2000)
i = n
j = n
print(creacion_tablero(n))
#t = random.randint(1, 10)
#print(t)
#gana_jugador_uno()
#if gana_jugador_uno() == True:
 #   print("jugador 1")
#else:
 #   print("jugador 2")
