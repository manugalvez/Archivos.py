# def suma():
#     num1=int(input("Ingrese un número: "))
#     num2=int(input("Ingrese otro número: "))
#     print(num1+num2)
    
# def resta():
#     num1=int(input("Ingrese un número: "))
#     num2=int(input("Ingrese otro número: "))
#     print(num1-num2)

# def multiplicacion():
#     num1=int(input("Ingrese un número: "))
#     num2=int(input("Ingrese otro número: "))
#     print(num1*num2)    

# def division():
#     num1=int(input("Ingrese un número: "))
#     num2=int(input("Ingrese otro número: "))
#     print(num1/num2)

# while True:
#     print("""
#           1- Suma
#           2- Resta
#           3- Multiplicacion
#           4- Division
#           5- Salir
#           """)
#     op=int(input("Selecciona una opción: "))
#     match op:
#         case 1:
#             suma()
#         case 2:
#             resta()
#         case 3:
#             multiplicacion()
#         case 4:
#             division()
#         case 5:
#             break
#         case _:
#             print("Seleccione opción válida")

#----------------------------------------------------------------------------------
# num=6

# if num>0 and num%2==0:
#     print("El número positivo y es par")
# else:
#     print("El número positivo o no es par")

#----------------------------------------------------------------------------------
# numEntrada=564
# entrada=True
# sitioEntrada="Ciudad Kainer"

# if numEntrada>300 and entrada==True and sitioEntrada=="Ciudad Kainer":
#     print("Puede entrar a la Ciudad Kainer")
# elif numEntrada>300 and entrada==True and sitioEntrada=="Ciudad Kainer":
#     print("Puede entrar al Museo")
# elif entrada==False:
#     print("No puede entrar")    

# llave="blue"

# if llave=="blue" or llave=="red" or llave=="white" or llave=="black":
#     print("Puede acceder")
# else:
#     print("No puede acceder")
    
#----------------------------------------------------------------------------------
# n = int(input("Introduce la altura del triángulo (entero positivo): "))
# for i in range(n):
#    print("*"*(i+1))

#----------------------------------------------------------------------------------
# Try:
# resultado=
# except :
#     print("")
# else:
#     print("")
# finally:
#     print("")

#----------------------------------------------------------------------------------
deuda=100000
opc=0
while True:
   print("""
          1- Pago con tarjeta de crédito
          2- Simulación de compras
          3- Salir
          """)
   opc=int(input("Selecciona una opción: "))
   match opc:
      case 1:
         print("Su deuda actual es de", deuda)
         print("Ingrese el monto a pagar")
         pago=int(input())
         if pago<=0 or pago>deuda:
            print("El pago debe ser mayor a 0 y menor que la deuda")
         else:
            deuda=deuda-pago
         print("El saldo a pagar es", deuda)
      case 2:
         while True:
            print("""
               Seleccione un objeto
               1. Monitor
               2. Teclado
               3. Laptop
               4. Salir
               """)
            opc=int(input("Selecciona una opción: "))
            match opc:
               case 1:
                  valor=80000
                  deuda=valor+deuda
                  print("Usted añadio un nuevo articulo, su nuevo saldo es",deuda)
               case 2:
                  valor=50000
                  deuda=valor+deuda
                  print("Usted añadio un nuevo articulo, su nuevo saldo es",deuda)
               case 3:
                  valor=1180000
                  deuda=valor+deuda
                  print("Usted añadio un nuevo articulo, su nuevo saldo es",deuda)
               case 4:
                  print("Gracias por su comprea")
                  break
               case _:
                  print("Seleccione opción válida")
      case 3:
         print("Gracias por usar el sistema de credito")
         break
      case _:
         print("Seleccione opción válida")
         
#----------------------------------------------------------------------------------


