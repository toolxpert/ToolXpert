try:
    import requests
    import sys
    import time
    from itertools import cycle
    import random
    import json
    import threading
    from datetime import datetime  # Import de datetime pour les dates et heures
except ImportError as e:
    print(f"Error importing modules: {e}")
    sys.exit(1)

# Définition des constantes
BEFORE = "["
AFTER = "]"
INPUT = ">"
reset = "\033[0m"
BEFORE_GREEN = "\033[92m["
AFTER_GREEN = "]"
GEN_VALID = "✅"
GEN_INVALID = "❌"
red = "\033[91m"
white = "\033[97m"
color = {"GREEN": "\033[92m"}

# Fonctions utilitaires
def current_time_hour():
    return datetime.now().strftime("%H:%M:%S")

def CheckWebhook(url):
    """Vérifie si l'URL du webhook est valide (accepte les formats discordapp.com et discord.com)"""
    return url.startswith("https://discord.com/api/webhooks/") or url.startswith("https://discordapp.com/api/webhooks/")

def Error(e):
    """Affiche une erreur générique"""
    print(f"An error occurred: {e}")
    sys.exit(1)

def ErrorNumber():
    """Affiche une erreur pour un nombre invalide de threads"""
    print("Invalid number of threads. Please enter a valid number.")
    sys.exit(1)

def ErrorWebhook():
    """Affiche une erreur pour un webhook invalide"""
    print("Invalid webhook URL. Please check and try again.")
    sys.exit(1)

# Programme principal
try:
    webhook_url = input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Webhook URL -> {reset}")
    
    # Vérifie si le webhook est valide
    if not CheckWebhook(webhook_url):
        ErrorWebhook()

    message = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Message -> {reset}")

    try:
        threads_number = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Threads Number -> {reset}"))
    except ValueError:
        ErrorNumber()

    def send_webhook():
        """Envoie le message au webhook"""
        headers = {'Content-Type': 'application/json'}
        payload = {
            'content': message,
            'username': "Webhook Spammer",
            'avatar_url': "https://example.com/avatar.png"
        }
        try:
            response = requests.post(webhook_url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()  # Lance une exception si la réponse est une erreur HTTP
            print(f"{BEFORE_GREEN + current_time_hour() + AFTER_GREEN} {GEN_VALID} Message: {white}{message}{color['GREEN']} Status: {white}Send{color['GREEN']}")
        except requests.exceptions.RequestException:
            print(f"{BEFORE + current_time_hour() + AFTER} {GEN_INVALID} Message: {white}{message}{red} Status: {white}Rate Limit{red}")

    def request():
        """Exécute les threads pour envoyer les webhooks"""
        threads = []
        for _ in range(threads_number):
            t = threading.Thread(target=send_webhook)
            t.start()
            threads.append(t)

        # Attendre que tous les threads se terminent
        for thread in threads:
            thread.join()

    # Boucle principale pour envoyer les messages
    while True:
        request()

except Exception as e:
    Error(e)
