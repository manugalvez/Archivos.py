#Matrices en una lista compuesta por listas
#          0    
#        0 1 2 
# listaM=[
#         [
#         [2,7,5],
#         [3,4,7,15]
#         ],
        
#         [
#         [9,1,2],
#         [8,6,71]
#         ]
#         ]
# print(listaM[1][1][0])
# for i in listaM:
#     print(i)

#----------------------------------------------------------
#Diccionario
# diccionario={"nombre": "Manuel Gálvez",
#     "fonos": [
#             98877882,
#             91209123,
#             80193712],
# "activo":True}
# producto={
#     "platano": 1400,
#     "pera"   : 1200,
#     "manzana": 1000,
#     "verduras": {'papa': 600, 'pepino': 500}
# }
# print(diccionario["activo"])
# for i in diccionario:
#     print(i)

# for clave, valor in producto.items():
#     print(f"{clave} = ${valor}")

#----------------------------------------------------------
# Nombres=[]
# for i in range(3):
#     Nom=input("Ingrese un nombre: ")
#     Nombres.append(Nom)

# mas=max(Nombres, key=len)
# print("El nombre más largo es",mas)

#----------------------------------------------------------
# nom={"Jake": "Armstrong", "Samuel": "Jackson", "Trevor": "Stacy"}

# for k, v in nom.items():
#     print(f"{k} {v}")

#----------------------------------------------------------
nom=[]
resp=""
while resp!="no":
    resp=input("Desea agregar un nombre? (si/no): ")
    if resp!="no":
        nn=input("Agregar nombre: ")
        nom.append(nn)
        
print(nom)
mas=max(nom, key=len)
nom.remove(mas)
print("El nombre eliminado fue", mas)
print(nom)