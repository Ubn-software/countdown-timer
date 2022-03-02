# pip install pyfiglet
import pyfiglet
from termcolor import colored

logo = pyfiglet.figlet_format("Ubn./") #Type here app/organisation name
print(colored(logo, 'yellow'))