from utils import color, io

def mostrar_menu():
    # Muestra las opciones disponibles
    io.imp_marco(""" ==GestArcCon== (Gestor de Archivos en Consola)
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
    pass

def crear_directorio():
    # Crea una nueva carpeta
    pass

def crear_archivo():
    # Crea un archivo de texto y permite escribir en él
    pass

def escribir_en_archivo():
    # Abre un archivo existente y añade texto al final
    pass

def eliminar_elemento():
    # Elimina un archivo o carpeta
    pass

def mostrar_informacion():
    # Muestra tamaño y fecha de modificación
    pass

def main():
    # Bucle principal del programa
    while True:
        mostrar_menu()
        try:
            opcion = io.leer_entero("Selecciona una opción: ", color.fore["INPUT"])
        except ValueError:
            io.imprimir("❌ Error: introduce un número del 1 al 7.", color.fore["ERROR"])
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
                io.imprimir("❌ Error: introduce un número del 1 al 7.", color.fore["ERROR"])

    io.imprimir("\nFin del programa.", color.fore["EXIT"])

if __name__ == '__main__':
    main()
