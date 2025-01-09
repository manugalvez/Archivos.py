#for i in range(3):
#    print("Saludos",i+5)
    
#total=0
#for i in range(3):
#    print("Ingrese gasto")
#    gasto=int(input())
#    total=total+gasto
#print("El total es ",total)


#for j in range(10):
#    for i in range(10):
#     print(j+1 ,"X",i+1,"=",(i+1)*(j+1))

#total=0
#for k in range(3):
#    print("Ingrese las notas")
#    nota=int(input())
#    total=total+nota
#print("Su promedio es ",total/(k+1))

#num=int(input("Ingrese un número: "))
#for i in range(num):
#    if i%2!=0:
#        print("El número es no par",i)

#pal="Manuel Gálvez"
#print(len(pal))

#for i in pal (pal):
#    print(i)

#total=0
#nom=input()
#for i in range(len(nom)):
#    total=total+(i+1)
    
#print("El total de la suma de sus numeros es ", total)

#lista=[55, 79, 4, 5, 6, 7, 8]

#for valor in lista:
#    print(valor)

#clave=616

#for i in range(3):
#    pas=int(input("Ingrese una contraseña: "))
#    if pas==clave:
#        print("Bienvenido a Skynet")
#        break
#    else:
#        print("Ha fallado intente nuevamente")

#print("No ha podido ingresar a Skynet, autodestrucción")
        
num=14

for i in range(5):
    pas=int(input("Ingrese una contraseña: "))
    if pas==num:
        print("Su número es correcto, el número es: ",num)
        break
    if pas > num:
        print("Su número es mayor, baje un poco más")
    if pas < num:
        print("Su número es menor, suba un poco más")
        
print("Fin")
