import os
import subprocess
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.progress import track
from time import sleep
from rich.color import Color
from rich import print

console = Console()
SCRIPT_PATH_DDOS = os.path.abspath(r"scripts\Brute.py")
SCRIPT_PATH_DISCORD = os.path.abspath(r"scripts\discord.py")
SCRIPT_PATH_DOXING = os.path.abspath(r"scripts\doxing-main.py")
EXE_PATH_SPOOF = os.path.abspath(r"scripts\spoof\Engine_Spoofer\Engine.exe")

def loading_animation(task_description):
    """
    Animation de chargement stylisée.
    """
    console.print(f"\n[cyan]{task_description}[/cyan]")
    for _ in track(range(30), description="[green]Chargement en cours...[/green]"):
        sleep(0.05)

def execute_script(script_path):
    """
    Exécute un script Python donné avec une animation.
    """
    if os.path.exists(script_path):
        console.print(f"\n[bold yellow][*] Exécution de : {os.path.basename(script_path)}[/bold yellow]\n")
        loading_animation("Préparation...")
        subprocess.run(["python", script_path])
    else:
        console.print(f"[bold red][!] Le script '{script_path}' n'existe pas.[/bold red]")

def open_exe(exe_path):
    """
    Ouvre un fichier exécutable donné.
    """
    if os.path.exists(exe_path):
        console.print(f"\n[bold yellow][*] Lancement de : {os.path.basename(exe_path)}[/bold yellow]\n")
        try:
            subprocess.run([exe_path], check=True)
        except subprocess.CalledProcessError as e:
            console.print(f"[bold red][!] Erreur lors de l'exécution de {exe_path}: {e}[/bold red]")
        except Exception as e:
            console.print(f"[bold red][!] Une erreur inattendue est survenue : {e}[/bold red]")
    else:
        console.print(f"[bold red][!] Le fichier exécutable '{exe_path}' n'existe pas.[/bold red]")

def display_header():
    """
    Affiche l'ASCII art personnalisé en guise d'en-tête.
    """
    art = """

$$$$$$$$\                  $$\ $$\   $$\                                $$\     
 \__$$  __|                 $$ |$$ |  $$ |                               $$ |    
     $$ | $$$$$$\   $$$$$$\  $$ |\$$\ $$  | $$$$$$\   $$$$$$\   $$$$$$\ $$$$$$\   
     $$ |$$  __$$\ $$  __$$\ $$ | \$$$$  / $$  __$$\ $$  __$$\ $$  __$$\\_$$  _|  
   $$ |$$ /  $$ |$$ /  $$ |$$ | $$  $$<  $$ /  $$ |$$$$$$$$ |$$ |  \__| $$ |    
       $$ |$$ |  $$ |$$ |  $$ |$$ |$$  /\$$\ $$ |  $$ |$$   ____|$$ |       $$ |$$\ 
       $$ |\$$$$$$  |\$$$$$$  |$$ |$$ /  $$ |$$$$$$$  |\$$$$$$$\ $$ |       \$$$$  |
      \__| \______/  \______/ \__|\__|  \__|$$  ____/  \_______|\__|        \____/ 
          $$ |                                   
          $$ |                                   
          \__|                                   
                            
                              
                              
  
    """
    console.print(art, style="bold green", justify="center")
    console.print("[bold cyan]Tool by 406 - Projet 406 V1[/bold cyan]", justify="center")
    console.print("[bold magenta]========================================[/bold magenta]\n", justify="center")

def main_menu():
    """
    Menu principal avec options stylisées.
    """
    while True:
        console.clear()
        display_header()
        menu_panel = Panel.fit(
            "[bold green]1.[/bold green] Attaque DDOS\n"
            "[bold green]2.[/bold green] Spoofer (perm admin)\n"
            "[bold green]3.[/bold green] Discord\n"
            "[bold green]4.[/bold green] Doxing\n"
            "[bold green]5.[/bold green] Quitter",
            title="[bold cyan]Options[/bold cyan]",
            border_style="bold magenta"
        )
        console.print(menu_panel, justify="center")

        choix = Prompt.ask("\n[bold magenta]Votre choix[/bold magenta]", choices=["1", "2", "3", "4"], default="4")

        if choix == '1':
            console.print("[bold cyan]\nVous avez choisi de lancer l'attaque DDoS ![/bold cyan]")
            execute_script(SCRIPT_PATH_DDOS)
            Prompt.ask("\n[bold magenta]Appuyez sur Entrée pour revenir au menu[/bold magenta]")
        elif choix == '2':
            console.print("[bold cyan]\nVous avez choisi d'ouvrir Engine.exe ![/bold cyan]")
            open_exe(EXE_PATH_SPOOF)
            Prompt.ask("\n[bold magenta]Appuyez sur Entrée pour revenir au menu[/bold magenta]")
        elif choix == '3':
            console.print("[bold cyan]\nVous avez choisi de lancer le menu discord ![/bold cyan]")
            execute_script(SCRIPT_PATH_DISCORD)
            Prompt.ask("\n[bold magenta]Appuyez sur Entrée pour revenir au menu[/bold magenta]")
        elif choix == '4':
            console.print("[bold cyan]\nVous avez choisi de lancer le menu doxing ![/bold cyan]")
            execute_script(SCRIPT_PATH_DOXING)
            Prompt.ask("\n[bold magenta]Appuyez sur Entrée pour revenir au menu[/bold magenta]")
        elif choix == '5':
            console.print("[bold green][*] Au revoir, et à bientôt ![/bold green]")
            break

if __name__ == "__main__":
    try:
        console.clear()
        display_header()
        loading_animation("Initialisation du programme...")
        main_menu()
    except Exception as e:
        console.print(f"[bold red]Une erreur est survenue : {e}[/bold red]")
        Prompt.ask("\n[bold magenta]Appuyez sur Entrée pour quitter[/bold magenta]")
