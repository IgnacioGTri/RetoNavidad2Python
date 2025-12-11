import json
import os

archivo = "CatalogoRegalos.json"

if os.path.exists(archivo):
    with open(archivo, "r", encoding="utf-8") as jason:
        datos = json.load(jason)

    if isinstance(datos, dict):
        datos = [datos]
else:
    datos = [] 
numArticulos = 0
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

print("¿Quieres añadir algún regalo más? S/N")