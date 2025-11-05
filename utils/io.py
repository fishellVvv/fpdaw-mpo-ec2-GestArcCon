from colorama import Style
from pathlib import Path
import os

''' funciones output '''

def imprimir(mensaje, color = None):
    if color != None:
        mensaje = color + mensaje + Style.RESET_ALL
    print(mensaje, end="")

def imp_marco(mensaje, color = None):
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

''' funciones input '''

def leer_entero(mensaje = "Introduce un número entero: ", color = None):
    try:
        imprimir(mensaje, color)
        entero = int(input())
    except ValueError:
        raise ValueError("Entrada no numérica")
    return entero

def leer_string(mensaje = "Introduce un texto: ", color = None):
    imprimir(mensaje, color)
    return input()

''' otras funciones '''

def pulsa_enter(color = None):
    if color != None:
        input(color + "\nPulsa enter para continuar..." + Style.RESET_ALL)
    else:
        input("\nPulsa enter para continuar...")

def obtener_extension(ruta, archivo):
    rutaArc = os.path.join(ruta, archivo)
    if os.path.isdir(rutaArc):
        return "dir"
    elif len(archivo.split(".")) == 1:
        return "file"
    else:
        return "." + archivo.split(".")[-1]

def ruta_actual(rutaBase):
    rutaRel = os.path.relpath(Path.cwd(), start=rutaBase)
    if rutaRel == ".":
        return "./"
    return f"./{Path(rutaRel).as_posix().strip('/')}/"

def tamanio_recursivo(rutaDir):
    tamanioTotal = 0
    numeroArchivos = 0

    contenido = os.listdir(rutaDir)
    for elemento in contenido:
        if elemento == ".git":
                continue
        ruta = os.path.join(rutaDir, elemento)

        if os.path.isfile(ruta):
            try:
                tamanioTotal += os.stat(ruta).st_size
                numeroArchivos += 1
            except (FileNotFoundError, PermissionError):
                pass

        if os.path.isdir(ruta):
            try:
                tamTotDir, numArcDir = tamanio_recursivo(ruta)
                tamanioTotal += tamTotDir
                numeroArchivos += numArcDir
            except (FileNotFoundError, PermissionError):
                pass

    return tamanioTotal, numeroArchivos
