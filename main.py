import subprocess
def ejecutar(comando):
    subprocess.run(comando)


print ("Creador de archivos y carpetas")
print ("1. Crear archivo de texto")
print ("2. Crear Carpeta: Calificaciones")
print ("3. Dentro de C. Calififcaciones, crear carpeta: Primer Parcial")
print ("4. Mover el archivo a la carpeta Calificaciones")
print ("5. Mover el programa a la carpeta Primer Parcial")

while true:
    opcion = input ("Elige una opción (1-5) o 'q' para salir:")
    
    if opcion =="1":
        ejectuar (["touch", "misnotas.txt"])
    elif opcion =="2":
        ejecutar (["mkdir", "calificaciones"])
    elif opcion =="3":
        ejecutar (["mkdir", "calificaciones/primer parcial"])
    elif opcion =="4":
        ejecutar (["mv", "misnotas.txt", "calificaciones"])
    elif opcion == "5":
        ejecutar (["mv", "programa.py", "calificaciones/primer_parcial/"])  
    elif opcion.lower()== "q":
        print ("Saliendo del programa...")
        break
    else:
        print ("Opción no válida, Por favor, elige una opción valida.")

