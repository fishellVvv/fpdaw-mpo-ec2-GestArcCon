from . import color
from colorama import Style
import os

''' funciones output '''

def imprimir(mensaje, color = None):
    # Aplica el color indicado y muestra el mensaje
    if color != None:
        mensaje = color + mensaje + Style.RESET_ALL
    print(mensaje, end="")

def imp_marco(mensaje, color = None):
    # Envuelve el mensaje en un marco, le aplica el color indicado y lo muestra
    frases = mensaje.split("\n")
    longFrase = [len(frase) for frase in frases]
    longMax = max(longFrase)
    msjMarco = ""
    for frase in frases:
        msjMarco += "│ " + frase + " " * (longMax - len(frase)) + " │\n"
    barraSup = "┌─" + "─" * longMax + "─┐" + "\n"
    barraInf = "└─" + "─" * longMax + "─┘"
    msjCompleto = barraSup + msjMarco + barraInf

    if color is not None:
        msjCompleto = color + msjCompleto + Style.RESET_ALL
    print(f"\n{msjCompleto}")

def mostrar_ruta_actual(rutaAct):
    # Da formato a la ruta proporcionada para mostrarla "truncada" y con los datos de su contenido, le aplica color y la muestra
    tamanioRutaActual, numeroArchivosRutaActual = tamanio_recursivo(rutaAct)

    pasosRuta = rutaAct.split(os.sep)
    
    if len(pasosRuta) > 3:
        rutaAct = os.sep.join([pasosRuta[0], "...", pasosRuta[-2], pasosRuta[-1]])
    
    imprimir("Ruta actual: ", color.fore["PATH"])
    imprimir(f"{rutaAct}")
    imprimir(f" [{tamanioRutaActual} bytes ({numeroArchivosRutaActual} archivos)]\n", color.fore["PATH"])

''' funciones input '''

def leer_entero(mensaje = "Introduce un número entero: ", color = color.fore["INPUT"]):
    # muestra el mensaje solicitando un entero aplicando color, lo lee, lo evalúa y lo devuelve
    try:
        imprimir(mensaje, color)
        entero = int(input())
    except ValueError:
        raise ValueError("Entrada no numérica")
    return entero

def leer_string(mensaje = "Introduce un texto: ", color = color.fore["INPUT"]):
    # muestra el mensaje solicitando un texto aplicando color, lo lee y lo devuelve
    imprimir(mensaje, color)
    return input()

''' otras funciones '''

def pulsa_enter(color = None):
    # Solicita un input pausando la ejecución
    if color != None:
        input(color + "\nPulsa enter para continuar..." + Style.RESET_ALL)
    else:
        input("\nPulsa enter para continuar...")

def obtener_extension(ruta, archivo):
    # Devuelve la extensión del archivo ("dir" si es un directorio y "file" si el archivo no tiene extensión)
    rutaArc = os.path.join(ruta, archivo)
    if os.path.isdir(rutaArc):
        return "dir"
    elif len(archivo.split(".")) == 1:
        return "file"
    else:
        return "." + archivo.split(".")[-1]

def tamanio_recursivo(rutaDir):
    # Calcula y devuelve el tamaño total de los archivos de una ruta y el número de estos
    # Este es el motivo por el cual se crea la restricción a no salir de la carpeta de trabajo
    tamanioTotal = 0
    numeroArchivos = 0

    try:
        contenido = os.listdir(rutaDir)
    except (FileNotFoundError, PermissionError):
        return 0, 0
    
    for elemento in contenido:
        rutaElem = os.path.join(rutaDir, elemento)

        if os.path.isfile(rutaElem):
            try:
                tamanioTotal += os.stat(rutaElem).st_size
                numeroArchivos += 1
            except (FileNotFoundError, PermissionError):
                pass

        if os.path.isdir(rutaElem):
            try:
                tamTotDir, numArcDir = tamanio_recursivo(rutaElem)
                tamanioTotal += tamTotDir
                numeroArchivos += numArcDir
            except (FileNotFoundError, PermissionError):
                pass

    return tamanioTotal, numeroArchivos

def comprobar_nombre(nombre):
    # Rechaza los nombres que contenga "/", "\" o que sean ".", ".." o vacío
    if "/" in nombre or "\\" in nombre:
        raise ValueError("Error: el nombre no puede ser una ruta\n")
    if nombre in ("", ".", ".."):
        raise ValueError("Error: nombre no válido\n")
    
def comprobar_txt(nombre):
    # Rechaza los nombres que no acaben en ".txt"
    if nombre.split(".")[-1] != "txt":
        raise ValueError("Error: el archivo debe ser .txt\n")
