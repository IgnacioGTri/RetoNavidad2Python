import json
import os

archivo = "Tienda.json"

if os.path.exists(archivo):
    with open(archivo, "r", encoding="utf-8") as jason:
        datos = json.load(jason)

    if isinstance(datos, dict):
        datos = [datos]
else:
    datos = []

cesta = []
total_compra = 0

pregunta = "S"

while pregunta == "S":

    articulo = input("Nombre del producto que quieres adquirir: ")

    encontrado = False

    for art in datos:
        if art["nombre"].lower() == articulo.lower():
            encontrado = True

            cantidad = int(input(f"¿Cuántos artículos quieres de {art['nombre']}?: "))

          
            if cantidad <= art["stock"]:
                precio_total = cantidad * art["precio"]

                print(f"Artículo disponible. Importe: {precio_total} €")

              
                cesta.append({
                    "nombre": art["nombre"],
                    "cantidad": cantidad,
                    "precio_unitario": art["precio"],
                    "precio_total": precio_total
                })

                art["stock"] -= cantidad
                total_compra += precio_total

            else:
                print(f"No hay suficiente stock. Stock disponible: {art['stock']}.")

            break

    if not encontrado:
        print("No disponemos de ese artículo en la Tienda.")

    pregunta = input("¿Quieres añadir algún artículo más? S/N ").upper()


with open(archivo, "w", encoding="utf-8") as jason:
    json.dump(datos, jason, indent=4, ensure_ascii=False)


print("\n--- RESUMEN DE LA COMPRA ---")

for compra in cesta:
    print(f"{compra['nombre']} x{compra['cantidad']} - {compra['precio_total']} €")

print(f"\nTotal a pagar: {total_compra} €")

print("\nStock actualizado y compra finalizada.")
print("¡Gracias por comprar en la Tienda!")
