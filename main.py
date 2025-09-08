from colorama import Fore, Style
import os
import sys
import time
import json
import subprocess
import random

user_game_file_path = 'user_data.json'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_data(key):
    try:
        with open(user_game_file_path, 'r') as file:
            data = json.load(file)
        if key in data:
            return data[key]
        else:
            raise KeyError(f"Key '{key}' not found.")
    except FileNotFoundError:
        print("Game data file not found. Loading default values.")
        time.sleep(1)
        return None
    except KeyError as e:
        print(e)

def save_data(key, value):
    try:
        with open(user_game_file_path, 'r+') as file:
            data = json.load(file)
            if key in data:
                data[key] = value
            else:
                print(f"Key '{key}' not found. Adding it at the top level.")
                data[key] = value
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()

    except FileNotFoundError:
        print("Game data file not found.")

if load_data('first_time') is None:
    default_data = {
        "first_time": False,
        "player_name": "Captain",
        "player_proffesion": None,
        "rank": 1,
        "credits": 1000,
        "inventory": [],
        "location": {
            "sector": "Alpha Quadrant",
            "station": "Deep Space 9",
            "exact_position": "Docking Port B",
        },
        "player_status": {
            "health": 100,
            "energy": 100,
            "hunger": 100,
            "thirst": 100,
            "fatigue": 100
        },
        "station_status": {
            "power": 100,
            "shields": 100,
            "hull": 100,
            "crew_morale": 100,
            "supplies": 100,
            "diplomacy": 100,
            "research": 100,
            "trade": 100,
            "infrastructure": 100,
            "security": 100,
            "medical": 100,
            "engineering": 100,
            "science": 100,
            "operations": 100,
            "communications": 100,
            "navigation": 100,
        },
        "diplomatic_relations": {
            "federation": 100,
            "klingons": 50,
            "romulans": 50
        }
    }
    with open(user_game_file_path, 'w') as file:
        json.dump(default_data, file, indent=4)

def status_bar():
    player_status = load_data('player_status') or {}
    player_location = load_data('location') or {}
    print(f"Sector: {Fore.CYAN}{player_location.get('sector', 'N/A')}{Style.RESET_ALL} | "
          f"Station: {Fore.LIGHTCYAN_EX}{player_location.get('station', 'N/A')}{Style.RESET_ALL} | "
          f"Position: {Fore.LIGHTMAGENTA_EX}{player_location.get('exact_position', 'N/A')}{Style.RESET_ALL} | "
          f"Credits: {Fore.YELLOW}{load_data('credits')}{Style.RESET_ALL} | "
          f"Health: {Fore.RED}{player_status.get('health', 'N/A')}{Style.RESET_ALL}% | "
          f"Energy: {Fore.GREEN}{player_status.get('energy', 'N/A')}{Style.RESET_ALL}% | "
          f"Hunger: {Fore.MAGENTA}{player_status.get('hunger', 'N/A')}{Style.RESET_ALL}% | "
          f"Thirst: {Fore.BLUE}{player_status.get('thirst', 'N/A')}{Style.RESET_ALL}% | "
          f"Fatigue: {Fore.YELLOW}{player_status.get('fatigue', 'N/A')}{Style.RESET_ALL}% |"
          f"Rank: {Fore.LIGHTBLUE_EX}{load_data('rank')}{Style.RESET_ALL} |"
          f"Proffesion: {Fore.LIGHTGREEN_EX}{load_data('player_proffesion')}{Style.RESET_ALL}")

def load_packages():
    current_dir = os.path.dirname(os.path.realpath(__file__))

    requirements_path = os.path.join(current_dir, 'requirements.txt')

    try:
        subprocess.check_output([sys.executable, "-m", "pip", "install", "-r", requirements_path])
    except subprocess.CalledProcessError:
        input('Something went wrong with PIP. Press enter to exit program...')
        sys.exit(1)

while True:
    clear()
    status_bar()
    print(Fore.LIGHTYELLOW_EX + "\n--- Main Menu ---" + Style.RESET_ALL)
    input("\nPress Enter to continue...")