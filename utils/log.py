from datetime import datetime

''' historial de comandos '''

def registrar_com(funcion, objetivo):
    hora = datetime.now().isoformat(timespec="seconds")
    linea = f"{hora} | {funcion} | {objetivo}\n"

    with open("log-com.txt", "a", encoding="utf-8") as log:
        log.write(linea)
