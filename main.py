from utils import color, io, log
from datetime import datetime
import os

rutaBase = os.path.join(os.getcwd(), "pruebas")

if not os.path.isdir(rutaBase):
    try:
        os.makedirs(rutaBase)
    except OSError as e:
        raise OSError(f"Error creando la carpeta de trabajo '{rutaBase}': {e.strerror}\n")
ruta = rutaBase

def mostrar_menu():
    # Muestra las opciones disponibles
    io.imp_marco("""           === GestArcCon ===
                 
1. Listar contenido del directorio actual
2. Crear un nuevo directorio
3. Crear un archivo de texto
4. Escribir texto en un archivo existente
5. Eliminar un archivo o directorio
6. Mostrar información del archivo
7. Renombrar un archivo o directorio
8. Navegar a otro directorio
9. Salir""",
    color.fore["MENU"])

def listar_contenido(rutaInt):
    # Lista archivos y carpetas del directorio actual
    try:
        contenido = os.listdir(rutaInt)

        carpetas = []
        archivos = []

        for elemento in contenido:
            rutaElem = os.path.join(rutaInt, elemento)

            if os.path.isdir(rutaElem):
                carpetas.append(elemento)
            else:
                archivos.append(elemento)
                
        carpetas.sort()
        archivos.sort()

        if len(carpetas + archivos) == 0:
            io.imprimir("\nEl directorio está vacío.")

        print()
        for elemento in carpetas + archivos:

            extension = io.obtener_extension(rutaInt, elemento)
            if extension != "dir":
                tipo = "archivo"
            else: 
                tipo = "carpeta"
            mensaje = f"{elemento} ({tipo})"
            
            io.imprimir(f"{mensaje}\n", color.colorear(extension))

        log.registrar_com("listar_contenido", rutaInt)
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: la ruta '{rutaInt}' no existe\n")

def crear_directorio(nombre):
    # Crea una nueva carpeta
    try:
        io.comprobar_nombre(nombre)

        rutaDir = os.path.join(ruta, nombre)

        os.mkdir(rutaDir)

        log.registrar_com("crear_directorio", rutaDir)
        return f"Directorio '{nombre}' creado con éxito.\n"
    except FileExistsError:
        raise FileExistsError(f"Error: el directorio '{nombre}' ya existe\n")

def crear_archivo(nombre):
    # Crea un archivo de texto y permite escribir en él
    try:
        io.comprobar_nombre(nombre)
        io.comprobar_txt(nombre)
        
        rutaArc = os.path.join(ruta, nombre)

        if os.path.exists(rutaArc):
            raise FileExistsError(f"Error: el archivo '{nombre}' ya existe\n")

        contenido = io.leer_string(f"Escribe en {nombre}: ").strip()
        with open(rutaArc, "x", encoding="utf-8") as archivo:
            archivo.write(contenido)

        log.registrar_com("crear_archivo", rutaArc)
        return f"Archivo '{nombre}' creado con éxito.\n"
    except FileExistsError:
        raise FileExistsError(f"Error: el archivo '{nombre}' ya existe\n")

def escribir_en_archivo(nombre):
    # Abre un archivo existente y añade texto al final
    try:
        io.comprobar_nombre(nombre)
        io.comprobar_txt(nombre)

        rutaArc = os.path.join(ruta, nombre)

        if not os.path.exists(rutaArc):
            raise FileNotFoundError(f"Error: el archivo '{nombre}' no existe\n")
        if os.path.isdir(rutaArc):
            raise IsADirectoryError(f"Error: '{nombre}' es un directorio\n")

        contenido = io.leer_string(f"Escribe en {nombre}: ").strip()
        with open(rutaArc, "a", encoding="utf-8") as archivo:
            archivo.write(f"\n{contenido}")

        log.registrar_com("escribir_en_archivo", rutaArc)
        return f"Archivo '{nombre}' modificado con éxito.\n"
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: el archivo '{nombre}' no existe\n")

def eliminar_elemento(nombre):
    # Elimina un archivo o carpeta
    try:
        io.comprobar_nombre(nombre)

        rutaElem = os.path.join(ruta, nombre)

        if not os.path.exists(rutaElem):
            raise FileNotFoundError(f"Error: el archivo o directorio '{nombre}' no existe\n")

        confirmacion = io.leer_string(f"Confirmar eliminación de {nombre} (S/N): ").strip()
        if confirmacion.lower() != "s":
            return f"Eliminación de '{nombre}' cancelada.\n"
        
        if os.path.isdir(rutaElem):
            try:
                os.rmdir(rutaElem)
            except OSError:
                raise OSError("Error: el directorio no está vacío\n")
            
            mensaje = f"Directorio '{nombre}' eliminado con éxito.\n"
        else:
            os.remove(rutaElem)
            mensaje = f"Archivo '{nombre}' eliminado con éxito.\n"

        log.registrar_com("eliminar_elemento", rutaElem)
        return mensaje
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: el archivo o directorio '{nombre}' no existe\n")

def mostrar_informacion(nombre):
    # Muestra tamaño y fecha de modificación
    try:
        io.comprobar_nombre(nombre)
        
        rutaElem = os.path.join(ruta, nombre)
        elemStat = os.stat(rutaElem)

        if os.path.isdir(rutaElem):
            tamanio, numeroArchivos = io.tamanio_recursivo(rutaElem)
            fecha_mod = datetime.fromtimestamp(elemStat.st_mtime).isoformat(timespec="seconds")
            mensaje = f"\nNombre: '{nombre}' | Tipo: directorio | Tamaño del contenido: {tamanio} bytes ({numeroArchivos} archivos) | Fecha de modificación: {fecha_mod} \n"
        else:
            extension = io.obtener_extension(ruta, nombre)
            tamanio = elemStat.st_size
            fechaMod = datetime.fromtimestamp(elemStat.st_mtime).isoformat(timespec="seconds")
            mensaje = f"\nNombre: '{nombre}' | Tipo: archivo ({extension}) | Tamaño: {tamanio} bytes | Fecha de modificación: {fechaMod} \n"

        log.registrar_com("mostrar_informacion", rutaElem)
        io.imprimir(mensaje, color.fore["INFO"])
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: el archivo o directorio '{nombre}' no existe\n")
    
def renombrar_elemento(nombre):
    # Renombra un archivo o carpeta
    try:
        io.comprobar_nombre(nombre)

        rutaElem = os.path.join(ruta, nombre)

        nuevoNombre = io.leer_string("\nIndica el nuevo nombre (con extensión si la tiene): ").strip()

        io.comprobar_nombre(nuevoNombre)

        rutaNuevoElem = os.path.join(ruta, nuevoNombre)

        if os.path.exists(rutaNuevoElem):
            raise FileExistsError("Error: ya existe un archivo o directorio con ese nombre\n")

        os.rename(rutaElem, rutaNuevoElem)

        log.registrar_com("renombrar_elemento", rutaNuevoElem)
        return f"Elemento '{nuevoNombre}' renombrado con éxito.\n"
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: el archivo o directorio '{nombre}' no existe\n")
    except FileExistsError:
        raise FileExistsError("Error: ya existe un archivo o directorio con ese nombre\n")
    except PermissionError:
        raise PermissionError("Error: permisos insuficientes para la operación solicitada\n")

def cambiar_ruta(nombre):
    # Navega hacia otra carpeta
    try:
        global ruta

        if nombre == "..":
            rutaNueva = os.path.dirname(ruta)
        elif nombre in (".", ""):
            rutaNueva = ruta
        else:
            rutaNueva = os.path.join(ruta, nombre)

        if not os.path.isdir(rutaNueva):
            raise FileNotFoundError(f"Error: el directorio '{nombre}' no existe\n")
        
        # protección para no salir de la carpeta de pruebas
        baseReal  = os.path.realpath(rutaBase)
        nuevaReal = os.path.realpath(rutaNueva)
        if os.path.commonpath([baseReal, nuevaReal]) != baseReal:
            raise PermissionError("Error: no se permite navegar fuera de la carpeta de trabajo\n")

        ruta = rutaNueva
        
        log.registrar_com("cambiar_ruta", rutaNueva)
        return f"Ruta actual actualizada con éxito.\n"
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: el archivo o directorio '{nombre}' no existe\n")

def main():
    # Bucle principal del programa
    log.registrar_com("INICIO", "GestArcCon")

    while True:
        mostrar_menu()
        io.mostrar_ruta_actual(ruta)

        try:
            opcion = io.leer_entero("\nSelecciona una opción: ")
        except ValueError:
            io.imprimir("Error: introduce un número del 1 al 9.\n", color.fore["ERROR"])
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
                    nombre = io.leer_string("\nIndica el nombre del nuevo directorio: ").strip()
                    io.imprimir(crear_directorio(nombre), color.fore["SUCCESS"])
                except Exception as e:
                    io.imprimir(str(e), color.fore["ERROR"])
                io.pulsa_enter()

            case 3:
                try:
                    nombre = io.leer_string("\nIndica el nombre del nuevo archivo (con extensión .txt): ").strip()
                    io.imprimir(crear_archivo(nombre), color.fore["SUCCESS"])
                except Exception as e:
                    io.imprimir(str(e), color.fore["ERROR"])
                io.pulsa_enter()

            case 4:
                try:
                    nombre = io.leer_string("\nIndica el nombre del archivo (con extensión .txt): ").strip()
                    io.imprimir(escribir_en_archivo(nombre), color.fore["SUCCESS"])
                except Exception as e:
                    io.imprimir(str(e), color.fore["ERROR"])
                io.pulsa_enter()

            case 5:
                try:
                    nombre = io.leer_string("\nIndica el nombre del directorio o archivo a eliminar (con extensión): ").strip()
                    io.imprimir(eliminar_elemento(nombre), color.fore["SUCCESS"])
                except Exception as e:
                    io.imprimir(str(e), color.fore["ERROR"])
                io.pulsa_enter()

            case 6:
                try:
                    nombre = io.leer_string("\nIndica el nombre del directorio o archivo a mostrar (con extensión): ").strip()
                    mostrar_informacion(nombre)
                except Exception as e:
                    io.imprimir(str(e), color.fore["ERROR"])
                io.pulsa_enter()

            case 7:
                try:
                    nombre = io.leer_string("\nIndica el nombre del directorio o archivo a renombrar (con extensión): ").strip()
                    io.imprimir(renombrar_elemento(nombre), color.fore["SUCCESS"])
                except Exception as e:
                    io.imprimir(str(e), color.fore["ERROR"])
                io.pulsa_enter()

            case 8:
                try:
                    nombre = io.leer_string("\nIndica el nombre del directorio al que navegar (navegar atrás con '..'): ").strip()
                    io.imprimir(cambiar_ruta(nombre), color.fore["SUCCESS"])
                except Exception as e:
                    io.imprimir(str(e), color.fore["ERROR"])
                io.pulsa_enter()

            case 9:
                io.imprimir("\nSaliendo...", color.fore["EXIT"])
                break

            case _:
                io.imprimir("Error: introduce un número del 1 al 9.\n", color.fore["ERROR"])
                io.pulsa_enter()

    io.imprimir("\nGracias por utilizar GestArcCon.\n\n", color.fore["EXIT"])
    log.registrar_com("CIERRE", "GestArcCon")

if __name__ == '__main__':
    main()
