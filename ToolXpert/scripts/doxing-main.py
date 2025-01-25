import os
import subprocess
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.progress import track
from time import sleep

console = Console()

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Chemins des scripts
SCRIPTS = {
    "phone-info": os.path.join(BASE_PATH, "scripts", "phone.py"),
    "email-info": os.path.join(BASE_PATH, "scripts", "Email-Tracker.py"),
    "username-tracker": os.path.join(BASE_PATH, "scripts", "Username-Tracker.py"),
    "soon": os.path.join(BASE_PATH, "scripts", "gen-nitro.py"),
    "soon": os.path.join(BASE_PATH, "scripts", "dm-delete.py"),
    "soon": os.path.join(BASE_PATH, "scripts", "raid.py"),
    "soon": os.path.join(BASE_PATH, "scripts", "spam-groupe.py"),
    "soon": os.path.join(BASE_PATH, "scripts", "token-login.py")
}

def loading_animation(task_description):
    """
    Affiche une animation de chargement stylisée.
    """
    console.print(f"\n[cyan]{task_description}[/cyan]")
    for _ in track(range(20), description="[green]Chargement...[/green]"):
        sleep(0.05)

def execute_script(script_key):
    """
    Exécute un script Python donné si le fichier existe.
    """
    script_path = SCRIPTS.get(script_key)
    if script_path and os.path.exists(script_path):
        console.print(f"[bold yellow]Exécution de : {os.path.basename(script_path)}[/bold yellow]")
        loading_animation("Préparation...")
        try:
            subprocess.run(["python", script_path], check=True)
        except subprocess.CalledProcessError as e:
            console.print(f"[bold red]Erreur d'exécution : {e}[/bold red]")
    else:
        console.print(f"[bold red]Le fichier '{script_path}' est introuvable.[/bold red]")

def display_header():
    """
    Affiche l'en-tête ASCII coloré.
    """
    console.print(r"""
[red] /$$$$$$$                      /$$                     [/red]
[red]| $$__  $$                    |__/                     [/red]
[red]| $$  \ $$  /$$$$$$  /$$   /$$ /$$ /$$$$$$$   /$$$$$$ [/red]
[red]| $$  | $$ /$$__  $$|  $$ /$$/| $$| $$__  $$ /$$__  $$[/red]
[red]| $$  | $$| $$  \ $$ \  $$$$/ | $$| $$  \ $$| $$  \ $$[/red]
[red]| $$  | $$| $$  | $$  >$$  $$ | $$| $$  | $$| $$  | $$[/red]
[red]| $$$$$$$/|  $$$$$$/ /$$/\  $$| $$| $$  | $$|  $$$$$$$[/red]
[red]|_______/  \______/ |__/  \__/|__/|__/  |__/ \____  $$[/red]
[red]                                            /$$  \ $$     [/red]  
[red]                                            |  $$$$$$/     [/red] 
[red]                                             \______/      [/red] 
""")
    console.print("[bold cyan]Tool by 406 - V1 ToolXpert [/bold cyan]")
    console.print("[bold cyan]==================================[/bold cyan]\n")


def main_menu():
    """
    Affiche et gère le menu principal.
    """
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_header()
        menu = (
            "1. Phone info\n"
            "2. Email info\n"
            "3. User name Tracker\n"
            "4. soon\n"
            "5. soon\n"
            "6. soon\n"
            "7. soon\n"
            "8. soon\n"
            "9. Quitter\n"
        )
        print(menu)

        choice = input("Votre choix: ")

        if choice == "1":
            execute_script("phone-info")
        elif choice == "2":
            execute_script("email-info")
        elif choice == "3":
            execute_script("username-tracker")
        elif choice == "4":
            execute_script("nitro_gen")
        elif choice == "5":
            execute_script("close_dm")
        elif choice == "6":
            execute_script("raid")
        elif choice == "7":
            execute_script("token-login")    
        elif choice == "8":
            execute_script("spam-groupe")    
        elif choice == "9":
            print("Quitter le programme...")
            break

        input("Appuyez sur Entrée pour revenir au menu")

if __name__ == "__main__":
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_header()
        loading_animation("Initialisation...")
        main_menu()
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
        input("Appuyez sur Entrée pour quitter")
