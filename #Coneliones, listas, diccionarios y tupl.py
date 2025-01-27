#Coneliones, listas, diccionarios y tuplas
#        0  1  2 3 4  5  -positivo
# lista = [1,76,65,9,7,54]
#       -6 -5 -4-3-2 -1  -negativo
# print(lista)

# print(lista)

# lista.sort()

# print(lista)

# lista.append(72)
# print(lista)

# for i in lista:
#     print("Elemnto",i)

# while True:
#     print(lista)
#     m=int(input("Agregue nuevo elemento: "))
#     lista.append(m)
#     print(lista)

# print(lista)

# lista.insert(9,"Cloud")
# print(lista)

# lista.insert(3,round(300.601))
# print(lista)

# lista.remove(76)
# print(lista)

# listaNom=["Pedro", "Juan", "Diego"]
# listaApe=["Rivera","Gonzales","Robles"]
# car=["Primer","Segundo","Tercer"]

# print(listaNom)

# listaNom.reverse()

# print(listaNom)

# for i in listaNom:
#     print(i)

# for i in listaNom:
#     print(len(listaNom))

# for i in range (len(listaNom)):
#     print("El",car[i],"nombre es:",listaNom[i], listaApe[i])

# for k in listaApe:
#     print(k)

# for k in listaNom:
#     print(len(listaApe))

# for k in range (len(listaApe)):
#     print(listaApe[k])


# while True:
#     print(listaNom)
#     print(listaApe)
#     n=input("Agregue nuevo elemento: ")
#     a=input("Agregue nuevo elemento: ")


# ListaFrutas=["Manzana","Platano","Coco","Pera","Durazno"]

# while True:
#     print(ListaFrutas)
#     m=input("Agregue una nueva fruta: ")
#     ListaFrutas.append(m)
#     print(ListaFrutas)
#     break

# ListaFrutas.remove("Durazno")
# print(ListaFrutas)


listaNom=["Pedro", "Juan", "Diego"]
listaFrutas=["Manzana","Platano","Coco","Pera","Durazno","Maracuya"]
listaPrecios=[1000,1150,1470,1400,1250,900]
c=1
Carrito=[]
Total=0

print("Quien va a ir a compar?")
for i in listaNom:
    print(c,'.-',i)
    c+=1
sel=int(input(">>> "))-1

print(listaNom[sel])

print("Bienvenido",listaNom[sel],"a la frutería")
while len(Carrito)<4:
    for frutas in range(len(listaFrutas)):
        print(frutas+1, ".-", listaFrutas[frutas])
    selFrutas=int(input("Seleccione una fruta: "))-1
    print("Usted a seleccionado",listaFrutas[selFrutas],"y su precio es",listaPrecios[selFrutas])
    Carrito.append(selFrutas)
    print(Carrito) 
print("Fruteria Dert")
for i in Carrito:
    print(f"",listaFrutas[i],"......",listaPrecios[i])
    Total=Total+listaPrecios[i]

print("Su total en la boleta es $",Total,"vuelva pronto",listaNom[sel])    
