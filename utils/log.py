from datetime import datetime
import os

''' historial de comandos '''

def registrar_com(funcion, objetivo):
    # Registra la actividad en el historial de comandos con hora, función y ruta
    hora = datetime.now().isoformat(timespec="seconds")
    linea = f"{hora} | {funcion} | {objetivo}\n"

    rutaLog = os.path.join(os.path.dirname(__file__), "log-com.txt")

    with open(rutaLog, "a", encoding="utf-8") as log:
        log.write(linea)
