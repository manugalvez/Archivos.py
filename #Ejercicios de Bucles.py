#Ejercicios de Bucles
#Ejercicio 1
#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

# word = input("Introduce una palabra: ")
# for i in range(10):
#     print(word)
    
#Ejercicio2 
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que 
# ha cumplido (desde 1 hasta su edad).

# age = int(input("¿Cuántos años tienes? "))
# for i in range(age):
#     print("Has cumplido " + str(i+1) + " años")
    
    
#Ejercicio3
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos 
# los números impares desde 1 hasta ese número separados por comas.   
 
n = int(input("Introduce un número entero positivo: "))
for i in range(1, n+1, 2):
    print(i, end=", ")

#Ejercicio4
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
# la cuenta atrás desde ese número hasta cero separados por comas.

n = int(input("Introduce un número entero positivo: "))
for i in range(n, -1, -1):
    print(i, end=", ")

#Ejercicio5
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el 
# número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura 
# la inversión.

amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años?"))
for i in range(years):
    amount *= 1 + interest / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2)))
    
#Ejercicio6
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
# rectángulo como el de más abajo, de altura el número introducido.
#*
#**
#***
#****
#*****

n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")

#Ejercicio7
#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")

#Ejercicio8
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo 
# como el de más abajo.
#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1

n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")

#Ejercicio9
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte 
# al usuario por la contraseña hasta que introduzca la contraseña correcta.

key = "contraseña"
password =""
while password != key:
    password = input("Introduce la contraseña: ")
print("Contraseña correcta")

#Ejercicio10
#Escribir un programa que pida al usuario un número entero positivo mayor que 2 y muestre 
# por pantalla si es un número primo o no.

n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")

#Ejercicio11
#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las 
# letras de la palabra introducida empezando por la última.

word = input("Introduce una palabra: ")
for i in range(len(word)-1, -1, -1):
    print(word[i])

#Ejercicio12
#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre 
# por pantalla el número de veces que aparece la letra en la frase.

frase = input("Introduce una frase: ")
letra = input("Introduce una letra")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))

#Ejercicio13
#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario 
# escriba “salir” que terminará.

while True:
    frase = input("Introduce algo: ")
    if frase == "salir":
        break
    print(frase)
