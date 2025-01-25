import requests
import random
from time import sleep
from colorama import Fore

def clear():
    print("\033c", end="")

def groupspamtitle():
    print(f"""{Fore.CYAN}

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
{Fore.RESET}""")

def proxy():
    # Ajoutez votre logique pour obtenir le proxy
    return None

def getheaders(token):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    return headers

def main():
    print("Returning to main menu...")

def setTitle(title):
    print(f"\033]0;{title}\007")

def selector(token, users):
    clear()
    while True:
        try:
            response = requests.post(f'https://discordapp.com/api/v9/users/@me/channels', proxies=proxy(), headers=getheaders(token), json={"recipients": users})

            if response.status_code == 204 or response.status_code == 200:
                print(f"[{Fore.LIGHTGREEN_EX}!{Fore.RESET}] Created groupchat")
            elif response.status_code == 429:
                print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Rate limited ({response.json()['retry_after']}ms)")
            else:
                print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Error: {response.status_code}")
        except Exception:
            pass
        except KeyboardInterrupt:
            break
    main()

def randomizer(token, ID):
    while True:
        users = random.sample(ID, 2)
        try:
            response = requests.post(f'https://discordapp.com/api/v9/users/@me/channels', proxies={"http": f'{proxy()}'}, headers=getheaders(token), json={"recipients": users})

            if response.status_code == 204 or response.status_code == 200:
                print(f"[{Fore.LIGHTGREEN_EX}!{Fore.RESET}] Created groupchat")
            elif response.status_code == 429:
                print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Rate limited ({response.json()['retry_after']}ms)")
            else:
                print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Error: {response.status_code}")
        except Exception:
            pass
        except KeyboardInterrupt:
            break
    main()

groupspamtitle()
print("Enter the token of the account you want to Spam")
token = input("Token: ")

print('\nDo you want to choose user(s) yourself to groupchat spam or do you want to select randoms?')
print('''
[01] choose user(s) yourself
[02] randomize the users
                    ''')
secondchoice = int(input('Choice: '))

if secondchoice not in [1, 2]:
    input(f'[!]{Fore.LIGHTRED_EX} Invalid Second Choice{Fore.RESET}')
    main()

if secondchoice == 1:
    setTitle("Creating groupchats")
    print('\nInput the users you want to create a groupchat with (separate by , id,id2,id3)')
    recipients = input('Users ID: ')
    user = recipients.split(',')
    if "," not in recipients:
        input(f"\n[!]{Fore.LIGHTRED_EX} You didn't have any commas (,) format is id,id2,id3{Fore.RESET}")
        main()
    input('\n\n\nPress enter to continue ("ctrl + c" at anytime to stop)')
    selector(token, user)

elif secondchoice == 2:
    setTitle("Creating groupchats")
    IDs = []
    friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", proxies={"http": f'http://{proxy()}'}, headers=getheaders(token)).json()
    for friend in friendIds:
        IDs.append(friend['id'])
    input('Press enter to continue ("ctrl + c" at anytime to stop)')
    randomizer(token, IDs)
