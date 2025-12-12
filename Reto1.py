import json
import os
import csv

archivo = "CatalogoRegalos.json"

if os.path.exists(archivo):
    with open(archivo, "r", encoding="utf-8") as jason:
        datos = json.load(jason)

    if isinstance(datos, dict):
        datos = [datos]
else:
    datos = [] 

print("1.Catálogo de regalos en JSON.")
for i in range (6):
    nombre = input("Introduce nombre del artículo: ")
    precio = float(input("Introduce precio: "))
    cantidad = int((input("Introduce cantidad de articulos: ")))


    articuloNuevo = {
        "nombre" : nombre,
        "precio" : precio,
        "cantidad" : cantidad
    }
    datos.append(articuloNuevo)

    with open ("CatalogoRegalos.json", "w", encoding="utf-8") as jason:
         json.dump(datos, jason, indent=4, ensure_ascii= False)
    print("Datos Guardados correctamente")


with open(archivo, "r", encoding="utf-8") as jason:
    contenido= jason.read()


print("\nTu lista de artículos Navideños:")
print(contenido)

respuesta = "S"
pregunta = "S"

while pregunta == "S":
    pregunta = input("¿Quieres añadir algún regalo más? S/N ").upper()

    if pregunta == "S":

       
        if os.path.exists(archivo):
            with open(archivo, "r", encoding="utf-8") as jason:
                datos = json.load(jason)
            if isinstance(datos, dict):
                datos = [datos]
        else:
            datos = []

        
        nombre = input("Introduce nombre del artículo: ")
        precio = float(input("Introduce precio: "))
        cantidad = int(input("Introduce cantidad de artículos: "))

        articuloNuevo = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }

        datos.append(articuloNuevo)

        with open(archivo, "w", encoding="utf-8") as jason:
            json.dump(datos, jason, indent=4, ensure_ascii=False)

        print("Artículo añadido correctamente.\n")
        
while respuesta == "S" :
    respuesta= input("¿Quieres cambiar el precio de un artículo?(S/N)").upper()
    
    if respuesta != "S":
        break
    
    if respuesta == "S":
         nombre_buscar = input("Introduce el nombre del regalo a rectificar: ")

    encontrado = False
    for art in datos:
        if art["nombre"].lower() == nombre_buscar.lower():
            nuevo_precio = float(input("Introduce el nuevo precio: "))
            art["precio"] = nuevo_precio
            encontrado = True
            break

    if encontrado:
        with open(archivo, "w", encoding="utf-8") as jason:
            json.dump(datos, jason, indent=4, ensure_ascii=False)
        print("Precio actualizado correctamente.")
    else:
        print("No se encontró un artículo con ese nombre.")
        
total = 0
for art in datos:
    total += art["precio"] * art["cantidad"]
    

print("\n2.Presupuesto navideño.")
presupuesto = input(f"¿De cuánto es tu presupuesto?")

print(f"\nPrecio total de todos los regalos: {total:.2f} €")

final = float(presupuesto) - total
if final >=0:
    print(f"Tu presupuesto final tras las compras es de {final} €")
else:
    print(f"No tienes suficiente, te quedarías a {final} €")
    

print("\n3.Sorteo de amigo invisible")
archivo2 = "personas.csv"
amigos=[]
with open (archivo2, "r", encoding="utf-8") as reparto:
    invisible = csv.reader(reparto)
    for fila in invisible:
        if fila:
            amigos.append(fila[0])

print("\nParejas para el amigo invisible: ")
for i in range(len(amigos)):
    print(f"{amigos[i]} le regalará a {amigos[(i +1) % len(amigos)]}")            

print("\n¡Adiós! ¡Felices Fiestas!")