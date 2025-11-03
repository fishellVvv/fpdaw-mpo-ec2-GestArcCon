from colorama import Fore

''' color '''

fore = {
    "MENU": Fore.BLUE,
    "PATH": Fore.LIGHTCYAN_EX,
    "EXIT": Fore.RED,
    "SUCCESS": Fore.LIGHTGREEN_EX,
    "ERROR": Fore.LIGHTRED_EX,
    "INPUT": Fore.LIGHTYELLOW_EX,
    "CONTINUE": Fore.LIGHTWHITE_EX
}

def colorear(extension):
    if extension == "dir":
        return Fore.MAGENTA
    elif extension == ".txt":
        return Fore.BLUE
    elif extension in [".jpg", ".png"]:
        return Fore.GREEN
    elif extension in [".mp3", ".wav"]:
        return Fore.YELLOW
    else:
        return Fore.WHITE
