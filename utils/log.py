from datetime import datetime

''' historial de comandos '''

def registrar_com(funcion, objetivo):
    time = datetime.now().isoformat(timespec="seconds")
    linea = f"{time} | {funcion} | {objetivo}\n"

    with open("log-com.txt", "a", encoding="utf-8") as log:
        log.write(linea)
