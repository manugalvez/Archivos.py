import random

def dado():
    return random.randint(1,6)
# num=dado()
# print(dado())*2

camino1=0
camino2=0
jugador=None
meta=24
print("Bienvenido al juedo de ludo")
print("¿Cuantos jugadores iniciarán?")
cantjugadores=int(input())

while True:
    for i in range(cantjugadores):
        print("Turno del jugador",i+1)
        print("¿Va a tirar el dado?")
        des=input()
        if des=="si":
            lado=dado()
            meta=meta-lado
            print("Has sacado el número", lado)
            camino1=camino1+lado
            print("Ha avanzado a la siguiente casilla, le falta", meta)
            break
        elif des=="no":
            print("Tu cedes el turno al siguiente jugador")
            print("Turno del jugador",i+1)
            lado=dado()
            meta=meta-lado
            print("Has sacado el número", lado)
            camino1=camino1+lado
            print("Ha avanzado a la siguiente casilla, le falta", meta)
            break
        else:
            print("¡Felcididades!")
            break

#----------------------------------------------------------------------------------
