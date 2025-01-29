#Usar lista o diccionario para ingresar nombre y edad de una persona

# ListaNom={}

# while True:
#     nombres=input("Agregue un nombre nombre: ")
#     personas[nombres]=edades
#     resp=input("Desea agregar un nombre? (si/no): ")
#     if resp=="x":
#       break
#     edades=input("Agregue la edad de {nombres}: ")
#       while
#      ListaNom[nombres]=int(edad) 

# print(f"\nLista de nombres y sus edades")
# for nombres, edad in ListaNom.items().
#     print(F"{nombres}: {edades} años")

#----------------------------------------------------------------
# Fut="Algo mas de texto"

# Lista=["Sephiroth", "Cloud", "Tifa", ""]

# with open('mi_archivo.txt','w') as archivo:
#     for i in Lista:
#         archivo.write(f"{i}\n")

#----------------------------------------------------------------    
# archivo=open('mi_archivo.txt','r')
# contenido=archivo.read()
# print(contenido)
# archivo.close()

#----------------------------------------------------------------
# import json
# datos={}


# with open('archivo.json', 'w') as archivo:
#     json.dump(datos, archivo)

#----------------------------------------------------------------
carrito=[]
frutas=["uva", "pera", "manzana"]
pf=[1100,1000,1200]
t=0
while True:
    print("""
          1.- Comprar
          2.- Pagar
          3.- Salir
        """)
    op=int(input("Seleccione una opción: "))
    match op:
        case 1:
            for i in range(len(frutas)):
                print(i+1,".-",frutas[i], "= $",pf[i])
            sel=int(input("Seleccione los prductos a comprar: "))
            carrito.append(sel-1)
            print(carrito)
        case 2:
            print("Verduderia Skrull de la fruta")
            print("-----------------------------")
            with open('boleta.txt','w') as archivo:
                archivo.write("Verduderia Skrull de la fruta\n")
                archivo.write("-----------------------------\n")
                for i in carrito:
                    archivo.write(f"{frutas}****${pf[i]}\n")
                archivo.write("-----------------------------\n")
            for i in carrito:
                t=t+pf[i]
            t_iva=t*0.19
            tt=t+t_iva
            archivo.write(f"Total {t}\n")
            archivo.write(f"Total Iva {t_iva}\n")
            archivo.write(f"Total a pagar {tt}\n")
            archivo.write("Gracias por su compra\n")
        case 3:
            break
        case _:
            print("Eleción no valida, seleccione de 1 a 3")
        
    print()
        
        

#----------------------------------------------------------------
# cliente="Shinichi Kurosaki"
# fecha="12/09/2000"
# producto=[
#     {"nombre":"Producto 1",     
#      "nombre":"Producto 2",
#      "nombre":"Producto 3",        
#     }
# ]

# def total(producto):
#     total=0
#     for producto


# total=total(producto)

# boleta=f"""

# Boleta de venta
# Cliente:
# Fecha:

# Detalles de los productos:
# """