import os
import subprocess
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.progress import track
from time import sleep


console = Console()


BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


SCRIPTS = {
    "nuker": os.path.join(BASE_PATH, "scripts", "nuker.py"),
    "webhook_spam": os.path.join(BASE_PATH, "scripts", "Whebook-spam.py"),
    "mass_dm": os.path.join(BASE_PATH, "scripts", "mass-dm.py"),
    "nitro_gen": os.path.join(BASE_PATH, "scripts", "gen-nitro.py"),
    "close_dm": os.path.join(BASE_PATH, "scripts", "dm-delete.py"),
    "raid": os.path.join(BASE_PATH, "scripts", "raid.py"),
    "spam-groupe": os.path.join(BASE_PATH, "scripts", "spam-groupe.py"),
    "token-login": os.path.join(BASE_PATH, "scripts", "token-login.py")
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
    Affiche l'en-tête ASCII.
    """
    art = r"""
$$$$$$$\  $$\                                               $$\ 
$$  __$$\ \__|                                              $$ |
$$ |  $$ |$$\  $$$$$$$\  $$$$$$$\  $$$$$$\   $$$$$$\   $$$$$$$ |
$$ |  $$ |$$ |$$  _____|$$  _____|$$  __$$\ $$  __$$\ $$  __$$ |
$$ |  $$ |$$ |\$$$$$$\  $$ /      $$ /  $$ |$$ |  \__|$$ /  $$ |
$$ |  $$ |$$ | \____$$\ $$ |      $$ |  $$ |$$ |      $$ |  $$ |
$$$$$$$  |$$ |$$$$$$$  |\$$$$$$$\ \$$$$$$  |$$ |      \$$$$$$$ |
\_______/ \__|\_______/  \_______| \______/ \__|       \_______|                                              
"""
    console.print(art, style="bold green", justify="center")
    console.print("[bold cyan]Tool by 406 - V1 ToolXpert[/bold cyan]", justify="center")
    console.print("[bold magenta]==================================[/bold magenta]\n", justify="center")

def main_menu():
    """
    Affiche et gère le menu principal.
    """
    while True:
        console.clear()
        display_header()
        menu = Panel.fit(
            "[bold blue]1.[/bold blue] token nuker\n"
            "[bold blue]2.[/bold blue] webhook spam\n"
            "[bold blue]3.[/bold blue] mass dm\n"
            "[bold blue]4.[/bold blue] Discord Nitro Generator\n"
            "[bold blue]5.[/bold blue] close dm\n"
            "[bold blue]6.[/bold blue] raid\n"
            "[bold blue]7.[/bold blue] token-login\n"
            "[bold blue]8.[/bold blue] spam-groupe\n"
            "[bold blue]9.[/bold blue] Quitter",
            title="[bold cyan]Menu Principal[/bold cyan]",
            border_style="bold magenta"
        )
        console.print(menu, justify="center")

        choice = Prompt.ask("\n[bold green]Votre choix[/bold green]", choices=["1", "2", "3", "4", "5", "6", "7", "8", "9"], default="7")

        if choice == "1":
            execute_script("nuker")
        elif choice == "2":
            execute_script("webhook_spam")
        elif choice == "3":
            execute_script("mass_dm")
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
            console.print("[bold red]Quitter le programme...[/bold red]")
            break

        Prompt.ask("\n[bold magenta]Appuyez sur Entrée pour revenir au menu[/bold magenta]")

if __name__ == "__main__":
    try:
        console.clear()
        display_header()
        loading_animation("Initialisation...")
        main_menu()
    except Exception as e:
        console.print(f"[bold red]Une erreur est survenue : {e}[/bold red]")
        Prompt.ask("\n[bold magenta]Appuyez sur Entrée pour quitter[/bold magenta]")
