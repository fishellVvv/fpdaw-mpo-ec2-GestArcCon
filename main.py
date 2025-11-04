from utils import color, io, log
from pathlib import Path
import os

rutaBase = Path.cwd()
ruta = io.ruta_actual(rutaBase)

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

def listar_contenido(rutaInt):
    # Lista archivos y carpetas del directorio actual
    try:
        archivos = os.listdir(rutaInt)
        print()
        for archivo in archivos:
            io.imprimir(archivo, color.colorear(io.obtener_extension(rutaInt, archivo)))
            print()
    except FileNotFoundError:
        raise FileNotFoundError(f"❌ Error: la ruta {rutaInt} no existe\n")

def crear_directorio(rutaInt):
    # Crea una nueva carpeta
    nombre = io.leer_string("\nIndica el nombre de la nueva carpeta: ", color.fore["INPUT"]).strip()
    try:
        os.mkdir(os.path.join(rutaInt, nombre))
        mensaje = f"✅ Carpeta {nombre} creada con exito.\n"
        mColor = color.fore["SUCCESS"]
        return mensaje, mColor
    except FileExistsError:
        raise FileExistsError(f"❌ Error: la carpeta {nombre} ya existe\n")

def crear_archivo():
    # Crea un archivo de texto y permite escribir en él
    io.imprimir("crear_archivo()\n")

def escribir_en_archivo():
    # Abre un archivo existente y añade texto al final
    io.imprimir("escribir_en_archivo()\n")

def eliminar_elemento():
    # Elimina un archivo o carpeta
    io.imprimir("eliminar_elemento()\n")

def mostrar_informacion():
    # Muestra tamaño y fecha de modificación
    io.imprimir("mostrar_informacion()\n")

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
                try:
                    listar_contenido(ruta)
                except Exception as e:
                    io.imprimir(str(e), color.fore["ERROR"])
                
                log.registrar_com("listar_contenido", ruta)
                io.pulsa_enter()
            case 2:
                try:
                    mensaje, mColor = crear_directorio(ruta)
                    io.imprimir(mensaje, mColor)
                except Exception as e:
                    io.imprimir(str(e), color.fore["ERROR"])
                
                log.registrar_com("crear_directorio", ruta)
                io.pulsa_enter()
            case 3:
                crear_archivo()

                log.registrar_com("crear_archivo", ruta)
                io.pulsa_enter()
            case 4:
                escribir_en_archivo()

                log.registrar_com("escribir_en_archivo", ruta)
                io.pulsa_enter()
            case 5:
                eliminar_elemento()

                log.registrar_com("eliminar_elemento", ruta)
                io.pulsa_enter()
            case 6:
                mostrar_informacion()

                log.registrar_com("mostrar_informacion", ruta)
                io.pulsa_enter()
            case 7:
                io.imprimir("\nSaliendo...", color.fore["EXIT"])
                break
            case _:
                io.imprimir("❌ Error: introduce un número del 1 al 7.\n", color.fore["ERROR"])
                io.pulsa_enter()

    io.imprimir("\nGracias por utilizar GestArcCon.\n\n", color.fore["EXIT"])

if __name__ == '__main__':
    main()
