import random
tablero = [[]]
t = random.randint(1, 10) #numero de juegos a jugar
n = random.randint(2, 2000) #tamaño del tablero
r1 = random.randint(1, n) #fila de las torres del jugador 1
r2 = random.randint(1, n) #fila de las torres del jugador 2

#creacion del tablero
def creacion_tablero(n):
    i = n
    j = n
    tablero[i][j] = " "
    for i in range(n):
        for j in range(n):
            tablero.append("a")
    return tablero



n = random.randint(2, 2000)
i = n
j = n
creacion_tablero(n)

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

t = random.randint(1, 10)
print(t)
gana_jugador_uno()
if gana_jugador_uno() == True:
    print("jugador 1")
else:
    print("jugador 2")
