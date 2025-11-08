from colorama import Fore, init
init(autoreset=True)

''' color '''

fore = {
    # Define los estilos de color por funcionalidad
    "MENU": Fore.BLUE,
    "PATH": Fore.LIGHTBLACK_EX,
    "INFO": Fore.GREEN,
    "EXIT": Fore.RED,
    "SUCCESS": Fore.LIGHTGREEN_EX,
    "ERROR": Fore.LIGHTRED_EX,
    "INPUT": Fore.LIGHTYELLOW_EX,
}

def colorear(extension):
    # Devuelve el color por tipo de elemento
    if extension == "dir":
        return Fore.CYAN
    elif extension == ".txt":
        return Fore.GREEN
    else:
        return Fore.WHITE
