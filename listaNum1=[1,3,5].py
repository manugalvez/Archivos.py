# listaNum1=[1,3,5]
# listaNum2=[2,4]
# while True:
#     pares=int(input("Agregue nuevo elemento: "))
#     impares=int(input("Agregue nuevo elemento: "))
#     listaNum1.append(pares)
#     listaNum2.append(impares)
#     print(listaNum1)
#     print(listaNum2)
# num=8
# listaPares=[]
# listaImpares=[]    


# for i in range(num):
#     if (i+1)%2==0:
#         listaPares.append(i+1)
#     else:
#         listaImpares.append(i+1)
# print("Pares= ",listaPares)
# print("Impares= ",listaImpares)


# notas=[]
# while True:
#     nota=int(input("Ingresa las notas, psara salir ingrese 0: "))
#     if nota != 0:
#         notas.append(nota)
#     else:
#         promedio= sum(notas)/len(notas)
#         print("Proceso finalizado, su promedio es", promedio)
#         break


# c=1
# listaNomCompleto=["Pedro Rivera", "Juan Gonzales", "Diego Robles"]
# for i in listaNomCompleto:
#     print(c,'.-',i)
#     c+=1
# listaNomCompleto.sort()
# print(listaNomCompleto)
# listaNomCompleto.reverse()
# print(listaNomCompleto)


# ListaPatente=["G4033","H0194","K4712"]
# for i in ListaPatente:
#     print("La patente ya esta registrada")


# marcas=[]
# korn=""
# while korn!="0":
#     korn=input("Ingrese una marca: ")
#     marcas.append(korn)
    
# print(marcas)


# temperatura=[33,31,30,32,31,29,35,28,27,29]
# print(round(sum(temperatura)/len(temperatura)))

# print(temperatura)

# for i in temperatura:
#     #print(i+6)
#     if i>=30:
#         print(i,"Hace mucho calor")
#     else:
#         print(i,"Hace calor")


# import random
# #print(num)
# listaLoteria=[]
# for i in range(7):
#     num=random.randint(1,38)    
#     listaLoteria.append(num)
#     listaLoteria.sort()
# print(listaLoteria)


listaEquipoColo=[]
listaEquipoU=[]
opc=""
while opc!="0":
    print("Cual de los equipos desea agregar?, para salir presione (0)")
    opc=input()
    if opc=="colo" and opc!=0:
        NumJugador=int(input("Ingrese el numero del jugador: "))
        listaEquipoColo.append(NumJugador)
    elif opc=="u" and opc!=0:
        NumJugador=int(input("Ingrese el numero del jugador: "))
        listaEquipoU.append(NumJugador)    
    print(listaEquipoColo)
    print(listaEquipoU)
