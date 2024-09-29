#Crear el diccionario inicial
informacion_personal = {
    "nombre": "Keiko Yanacallo",
    "edad": 23,
    "ciudad":"Napo",
    "profesion": "Agricultora"
}

#Acceder al valor de "ciudad" y modificarlo
informacion_personal["ciudad"] ="El Chaco"

#Actualizar la clave de la profesión
informacion_personal["profesion"] = "Ingeniro"

#Verificar si la clave "telefono" existe y agregarla si no está
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "665-6798"

#Eliminar la clave "edad"
informacion_personal.pop("edad")

# Imprimir cada clave y valor usando iteración
print("Diccionario final:")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")