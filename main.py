from utils import color, io, log
import os

ruta = "./"

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
    io.imprimir(f"Ruta actual: {ruta}\n", color.fore["PATH"])

def listar_contenido():
    # Lista archivos y carpetas del directorio actual
    try:
        archivos = os.listdir(ruta)
        print()
        for archivo in archivos:
            io.imprimir(archivo, color.colorear(io.obtener_extension(ruta, archivo)))
            print()
    except FileNotFoundError:
        io.imprimir(f"❌ Error: la ruta {ruta} no existe\n", color.fore["ERROR"])

    log.registrar_com("listar_contenido", ruta)
    io.pulsa_enter()

def crear_directorio():
    # Crea una nueva carpeta
    io.imprimir("crear_directorio()\n")
    log.registrar_com("crear_directorio", ruta)
    io.pulsa_enter()

def crear_archivo():
    # Crea un archivo de texto y permite escribir en él
    io.imprimir("crear_archivo()\n")
    log.registrar_com("crear_archivo", ruta)
    io.pulsa_enter()

def escribir_en_archivo():
    # Abre un archivo existente y añade texto al final
    io.imprimir("escribir_en_archivo()\n")
    log.registrar_com("escribir_en_archivo", ruta)
    io.pulsa_enter()

def eliminar_elemento():
    # Elimina un archivo o carpeta
    io.imprimir("eliminar_elemento()\n")
    log.registrar_com("eliminar_elemento", ruta)
    io.pulsa_enter()

def mostrar_informacion():
    # Muestra tamaño y fecha de modificación
    io.imprimir("mostrar_informacion()\n")
    log.registrar_com("mostrar_informacion", ruta)
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
                io.imprimir("\nSaliendo...", color.fore["EXIT"])
                break
            case _:
                io.imprimir("❌ Error: introduce un número del 1 al 7.\n", color.fore["ERROR"])
                io.pulsa_enter()

    io.imprimir("\nGracias por utilizar GestArcCon.\n\n", color.fore["EXIT"])

if __name__ == '__main__':
    main()
