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
    long_frase = [len(frase) for frase in frases]
    long_max = max(long_frase)
    msj_marco = ""
    for frase in frases:
        msj_marco += "│ " + frase + " " * (long_max - len(frase)) + " │\n"
    barra_sup = "┌─" + "─" * long_max + "─┐" + "\n"
    barra_inf = "└─" + "─" * long_max + "─┘"
    msj_completo = barra_sup + msj_marco + barra_inf

    if color is not None:
        msj_completo = color + msj_completo + Style.RESET_ALL
    print(msj_completo)

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
    if os.path.isdir(ruta+archivo):
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
