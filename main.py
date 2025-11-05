from utils import color, io, log
from datetime import datetime
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

def listar_contenido(rutaInt):
    # Lista archivos y carpetas del directorio actual
    try:
        contenido = os.listdir(rutaInt)

        carpetas = []
        archivos = []

        for nombre in contenido:
            if nombre == ".git":      # opcional
                continue
            ruta = os.path.join(rutaInt, nombre)

            if os.path.isdir(ruta):
                carpetas.append(nombre)
            else:
                archivos.append(nombre)

        carpetas.sort()
        archivos.sort()

        print()
        for elemento in carpetas + archivos:

            if io.obtener_extension(rutaInt, elemento) != "dir":
                tipo = "archivo"
            else: 
                tipo = "carpeta"

            mensaje = f"{elemento} ({tipo})"
            io.imprimir(mensaje, color.colorear(io.obtener_extension(rutaInt, elemento)))
            print()

        log.registrar_com("listar_contenido", rutaInt)
    except FileNotFoundError:
        raise FileNotFoundError(f"❌ Error: la ruta '{rutaInt}' no existe\n")

def crear_directorio(nombre):
    # Crea una nueva carpeta
    try:
        rutaDir = os.path.join(ruta, nombre)
        os.mkdir(rutaDir)

        log.registrar_com("crear_directorio", rutaDir)
        return f"✅ Directorio '{nombre}' creado con éxito.\n"
    except FileExistsError:
        raise FileExistsError(f"❌ Error: el directorio '{nombre}' ya existe\n")

def crear_archivo(nombre):
    # Crea un archivo de texto y permite escribir en él
    try:
        if len(nombre.split("/")) > 1:
            raise ValueError("❌ Error: el nombre del archivo no puede ser una ruta\n")
        rutaArc = os.path.join(ruta, nombre)

        contenido = io.leer_string(f"\nEscribe en {nombre}:\n", color.fore["INPUT"]).strip()
        with open(rutaArc, "x", encoding="utf-8") as archivo:
            archivo.write(contenido)

        log.registrar_com("crear_archivo", nombre)
        return f"✅ Archivo '{nombre}' creado con éxito.\n"
    except FileExistsError:
        raise FileExistsError(f"❌ Error: el archivo '{nombre}' ya existe\n")

def escribir_en_archivo(nombre):
    # Abre un archivo existente y añade texto al final
    try:
        if len(nombre.split("/")) > 1:
            raise ValueError("❌ Error: el nombre del archivo no puede ser una ruta\n")
        if nombre.split(".")[-1] != "txt":
            raise ValueError("❌ Error: el archivo debe ser .txt\n")
        rutaArc = os.path.join(ruta, nombre)

        contenido = io.leer_string(f"\nEscribe en {nombre}:\n", color.fore["INPUT"]).strip()
        with open(rutaArc, "a", encoding="utf-8") as archivo:
            archivo.write(f"\n{contenido}")

        log.registrar_com("escribir_en_archivo", nombre)
        return f"✅ Archivo '{nombre}' modificado con éxito.\n"
    except FileNotFoundError:
        raise FileNotFoundError(f"❌ Error: el archivo '{nombre}' no existe\n")

def eliminar_elemento(nombre):
    # Elimina un archivo o carpeta
    try:
        if nombre.split(".")[-1] == "py":
            raise ValueError("❌ Error: por seguridad no se permite eliminar archivos .py\n")
        rutaElem = os.path.join(ruta, nombre)

        confirmacion = io.leer_string(f"\nConfirmar eliminación de {nombre} (S/N): ", color.fore["INPUT"]).strip()
        if confirmacion.lower() != "s":
            return f"Eliminación de '{nombre}' cancelada.\n"
        
        if os.path.isdir(rutaElem):
            try:
                os.rmdir(rutaElem)
            except OSError:
                raise OSError("❌ Error: el directorio no está vacío\n")
            
            mensaje = f"✅ Directorio '{nombre}' eliminado con éxito.\n"
        else:
            os.remove(rutaElem)
            mensaje = f"✅ Archivo '{nombre}' eliminado con éxito.\n"

        log.registrar_com("eliminar_elemento", nombre)
        return mensaje
    except FileNotFoundError:
        raise FileNotFoundError(f"❌ Error: el archivo o directorio '{nombre}' no existe\n")

def mostrar_informacion(nombre):
    # Muestra tamaño y fecha de modificación
    try:
        rutaElem = os.path.join(ruta, nombre)
        elemStat = os.stat(rutaElem)

        if os.path.isdir(rutaElem):
            tamanio, numeroArchivos = io.tamanio_recursivo(rutaElem)
            fecha_mod = datetime.fromtimestamp(elemStat.st_mtime).isoformat(timespec="seconds")
            mensaje = f"Nombre: '{nombre}' | Tipo: directorio | Tamaño del contenido: {tamanio} bytes ({numeroArchivos} archivos) | Fecha de modificación: {fecha_mod} \n"
        else:
            extension = io.obtener_extension(ruta, nombre)
            tamanio = elemStat.st_size
            fechaMod = datetime.fromtimestamp(elemStat.st_mtime).isoformat(timespec="seconds")
            mensaje = f"Nombre: '{nombre}' | Tipo: archivo ({extension}) | Tamaño: {tamanio} bytes | Fecha de modificación: {fechaMod} \n"

        log.registrar_com("mostrar_informacion", nombre)
        io.imprimir(mensaje, color.fore["INFO"])
    except FileNotFoundError:
        raise FileNotFoundError(f"❌ Error: el archivo o directorio '{nombre}' no existe\n")

def main():
    # Bucle principal del programa
    while True:
        mostrar_menu()
        tamanioRutaActual, numeroArchivosRutaActual = io.tamanio_recursivo(ruta)
        io.imprimir(f"Ruta actual: {ruta}    [{tamanioRutaActual} bytes ({numeroArchivosRutaActual} archivos)]\n", color.fore["PATH"])
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
                    nombre = io.leer_string("\nIndica el nombre del nuevo archivo (sin extensión): ", color.fore["INPUT"]).strip() + ".txt"
                    io.imprimir(crear_archivo(nombre), color.fore["SUCCESS"])
                except Exception as e:
                    io.imprimir(str(e), color.fore["ERROR"])
                io.pulsa_enter()

            case 4:
                try:
                    nombre = io.leer_string("\nIndica el nombre del archivo (con extensión .txt): ", color.fore["INPUT"]).strip()
                    io.imprimir(escribir_en_archivo(nombre), color.fore["SUCCESS"])
                except Exception as e:
                    io.imprimir(str(e), color.fore["ERROR"])
                io.pulsa_enter()

            case 5:
                try:
                    nombre = io.leer_string("\nIndica el nombre del directorio o archivo (con extensión): ", color.fore["INPUT"]).strip()
                    io.imprimir(eliminar_elemento(nombre), color.fore["SUCCESS"])
                except Exception as e:
                    io.imprimir(str(e), color.fore["ERROR"])
                io.pulsa_enter()

            case 6:
                try:
                    nombre = io.leer_string("\nIndica el nombre del directorio o archivo (con extensión): ", color.fore["INPUT"]).strip()
                    mostrar_informacion(nombre)
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
