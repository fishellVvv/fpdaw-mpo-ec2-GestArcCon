from utils import color, io

def mostrar_menu():
    # Muestra las opciones disponibles
    io.imp_marco("""   === GestArcCon ===
                 
1. Listar contenido del directorio actual
2. Crear un nuevo directorio
3. Crear un archivo de texto
4. Escribir texto en un archivo existente
5. Eliminar un archivo o directorio
6. Mostrar información del archivo
7. Salir""",
    color.fore["MENU"])

def listar_contenido():
    # Lista archivos y carpetas del directorio actual
    io.imprimir("listar_contenido()\n")
    io.pulsa_enter()

def crear_directorio():
    # Crea una nueva carpeta
    io.imprimir("crear_directorio()\n")
    io.pulsa_enter()

def crear_archivo():
    # Crea un archivo de texto y permite escribir en él
    io.imprimir("crear_archivo()\n")
    io.pulsa_enter()

def escribir_en_archivo():
    # Abre un archivo existente y añade texto al final
    io.imprimir("escribir_en_archivo()\n")
    io.pulsa_enter()

def eliminar_elemento():
    # Elimina un archivo o carpeta
    io.imprimir("eliminar_elemento()\n")
    io.pulsa_enter()

def mostrar_informacion():
    # Muestra tamaño y fecha de modificación
    io.imprimir("mostrar_informacion()\n")
    io.pulsa_enter()

def main():
    # Bucle principal del programa
    while True:
        mostrar_menu()
        try:
            opcion = io.leer_entero("Selecciona una opción: ", color.fore["INPUT"])
        except ValueError:
            io.imprimir("❌ Error: introduce un número del 1 al 7.\n", color.fore["ERROR"])
            io.pulsa_enter()
            continue

        match opcion:
            case 1:
                listar_contenido()
            case 2:
                crear_directorio()
            case 3:
                crear_archivo()
            case 4:
                escribir_en_archivo()
            case 5:
                eliminar_elemento()
            case 6:
                mostrar_informacion()
            case 7:
                io.imprimir("Saliendo...", color.fore["EXIT"])
                break
            case _:
                io.imprimir("❌ Error: introduce un número del 1 al 7.\n", color.fore["ERROR"])
                io.pulsa_enter()

    io.imprimir("\nFin del programa. === GestArcCon ===\n", color.fore["EXIT"])

if __name__ == '__main__':
    main()
