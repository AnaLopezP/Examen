import random
tablero = [[]]
t = random.randint(1, 10) #numero de juegos a jugar
n = random.randint(2, 2000) #tamaño del tablero
r1 = random.randint(1, n)
r2 = random.randint(1, n)






#codigo principal
print(t)
if gana_jugador_uno() == True:
    print("jugador 1")
else:
    print("jugador 2")
