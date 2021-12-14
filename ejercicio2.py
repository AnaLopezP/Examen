import random
t = random.randint(1, 10) #numero de juegos a jugar
n = random.randint(2, 2000) #tamaño del tablero
r1 = random.randint(1, n) #fila de las torres del jugador 1
r2 = random.randint(1, n) #fila de las torres del jugador 2
tablero = []*n
#creacion del tablero
def creacion_tablero(n):
    n
    print(n)
    r1
    r2
    print(r1)
    print(r2)
    for i in range(n, n):
        for j in range(n, n):
            if tablero[i] == r1:
                tablero.append("T1")
            elif tablero[i] == r2:
                tablero.append("T2")
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
t = random.randint(1, 10)
print(t)
gana_jugador_uno()
while t !=0:
    creacion_tablero(n)
    if gana_jugador_uno() == True:
        print("jugador 1")
    else:
        print("jugador 2")
    t = t - 1
