
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


Title=("Discord Token Mass Dm")

try:
    def MassDM(token_discord, channels, Message):
        for channel in channels:
            for user in [x["username"]+"#"+x["discriminator"] for x in channel["recipients"]]:
                try:
                    requests.post(f"https://discord.com/api/v9/channels/{channel['id']}/messages", headers={'Authorization': token_discord}, data={"content": f"{Message}"})
                    print(f'{BEFORE + current_time_hour() + AFTER} {ADD} Status: {white}Send{red} User: {white}{user}{red}')

                except Exception as e:
                    print(f'{BEFORE + current_time_hour() + AFTER} {ERROR} Status: {white}Error: {e}{red}')

    Slow=(discord_banner)
    token_discord = Choice1TokenDiscord()
    validityTest = requests.get('https://discordapp.com/api/v6/users/@me', headers={'Authorization': token_discord, 'Content-Type': 'application/json'})
    if validityTest.status_code != 200:
        ErrorToken()
    try:
        message = str(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Message -> {reset}"))
    except:
        pass
    processes = []

    try:
        repetition = int(input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Number of Repetitions -> {reset}"))
    except:
        ErrorNumber()

    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers={'Authorization': token_discord}).json()

    number = 0
    for i in range(repetition):
        number += 1
        if not channelIds:
            ()
        for channel in [channelIds[i:i+3] for i in range(0, len(channelIds), 3)]:
            t = threading.Thread(target=MassDM, args=(token_discord, channel, message))
            t.start()
            processes.append(t)
        for process in processes:
            process.join()
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Finish n°{number}.")
        time.sleep(0.5)
        

    Continue()
    Reset()
except Exception as e:
    Error(e)