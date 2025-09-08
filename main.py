from colorama import Fore, Style
import os
import sys
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print(f"{Fore.GREEN}Welcome to DS9!{Fore.WHITE}")