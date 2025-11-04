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

        log.registrar_com("listar_contenido", rutaInt)
    except FileNotFoundError:
        raise FileNotFoundError(f"❌ Error: la ruta '{rutaInt}' no existe\n")

def crear_directorio(nombre):
    # Crea una nueva carpeta
    try:
        ruta_dir = os.path.join(ruta, nombre)
        os.mkdir(ruta_dir)

        log.registrar_com("crear_directorio", ruta_dir)
        return f"✅ Directorio '{nombre}' creado con exito.\n"
    except FileExistsError:
        raise FileExistsError(f"❌ Error: el directorio '{nombre}' ya existe\n")

def crear_archivo(nombre):
    # Crea un archivo de texto y permite escribir en él
    try:
        if len(nombre.split("/")) > 1:
            raise ValueError("❌ Error: el nombre del archivo no puede ser una ruta\n")
        ruta_archivo = os.path.join(ruta, nombre)
        open(ruta_archivo, "x")

        contenido = io.leer_string(f"\nEscribe en {nombre}:\n", color.fore["INPUT"]).strip()
        with open(ruta_archivo, "w") as archivo:
            archivo.write(contenido)

        log.registrar_com("crear_archivo", nombre)
        return f"✅ Archivo '{nombre}' creado con exito.\n"
    except FileExistsError:
        raise FileExistsError(f"❌ Error: el archivo '{nombre}' ya existe\n")

def escribir_en_archivo(nombre):
    # Abre un archivo existente y añade texto al final
    try:
        if len(nombre.split("/")) > 1:
            raise ValueError("❌ Error: el nombre del archivo no puede ser una ruta\n")
        if nombre.split(".")[-1] != "txt":
            raise ValueError("❌ Error: el archivo debe ser .txt\n")
        ruta_archivo = os.path.join(ruta, nombre)

        contenido = io.leer_string(f"\nEscribe en {nombre}:\n", color.fore["INPUT"]).strip()
        with open(ruta_archivo, "a") as archivo:
            archivo.write(f"\n{contenido}")

        log.registrar_com("escribir_en_archivo", nombre)
        return f"✅ Archivo '{nombre}' modificado con exito.\n"
    except FileNotFoundError:
        raise FileNotFoundError(f"❌ Error: el archivo '{nombre}' no existe\n")

def eliminar_elemento(nombre):
    # Elimina un archivo o carpeta
    
    log.registrar_com("eliminar_elemento", nombre)
    io.imprimir("eliminar_elemento()\n")

def mostrar_informacion(nombre):
    # Muestra tamaño y fecha de modificación
    
    log.registrar_com("mostrar_informacion", nombre)
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
                io.pulsa_enter()

            case 2:
                try:
                    nombre = io.leer_string("\nIndica el nombre del nuevo directorio: ", color.fore["INPUT"]).strip()
                    io.imprimir(crear_directorio(nombre), color.fore["SUCCESS"])
                except Exception as e:
                    io.imprimir(str(e), color.fore["ERROR"])
                io.pulsa_enter()

            case 3:
                try:
                    nombre = io.leer_string("\nIndica el nombre del nuevo archivo: ", color.fore["INPUT"]).strip() + ".txt"
                    io.imprimir(crear_archivo(nombre), color.fore["SUCCESS"])
                except Exception as e:
                    io.imprimir(str(e), color.fore["ERROR"])
                io.pulsa_enter()

            case 4:
                try:
                    nombre = io.leer_string("\nIndica el nombre del archivo: ", color.fore["INPUT"]).strip()
                    io.imprimir(escribir_en_archivo(nombre), color.fore["SUCCESS"])
                except Exception as e:
                    io.imprimir(str(e), color.fore["ERROR"])
                io.pulsa_enter()

            case 5:
                try:
                    io.imprimir(eliminar_elemento(nombre), color.fore["SUCCESS"])
                except Exception as e:
                    io.imprimir(str(e), color.fore["ERROR"])
                io.pulsa_enter()

            case 6:
                try:
                    io.imprimir(mostrar_informacion(nombre), color.fore["SUCCESS"])
                except Exception as e:
                    io.imprimir(str(e), color.fore["ERROR"])
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
