# Crear un nuevo archivo llamado my_notes.txt y escribir notas personales en él
with open('my_notes.txt', 'w') as file:
    # Escribiendo notas personales
    file.write("Esta es mi primera nota personal.\n")
    file.write("Hoy aprendí a manipular archivos de texto en Python.\n")
    file.write("Es un proceso muy útil para organizar mis notas.\n")

# Leer el contenido del archivo línea por línea
with open('my_notes.txt', 'r') as file:
    # Leer y mostrar cada línea en la consola
    for line in file:
        print(line.strip())  # Usamos strip() para eliminar saltos de línea

# No es necesario cerrar el archivo manualmente, ya que usamos 'with', que lo hace automáticamente.