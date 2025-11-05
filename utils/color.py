from colorama import Fore, init
init(autoreset=True)

''' color '''

fore = {
    "MENU": Fore.BLUE,
    "PATH": Fore.LIGHTBLACK_EX,
    "INFO": Fore.GREEN,
    "EXIT": Fore.RED,
    "SUCCESS": Fore.LIGHTGREEN_EX,
    "ERROR": Fore.LIGHTRED_EX,
    "INPUT": Fore.LIGHTYELLOW_EX,
}

def colorear(extension):
    if extension == "dir":
        return Fore.GREEN
    elif extension == ".txt":
        return Fore.CYAN
    else:
        return Fore.WHITE
