import json
import os
import csv


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
    actual =amigos[i]
    siguiente= amigos[(i +1) % len(amigos)]
    print(f"{actual} le regalará a {siguiente}")     

archivo3 = "ParejasAmigoInvisble"           

print("\n¡Adiós! ¡Felices Fiestas!")