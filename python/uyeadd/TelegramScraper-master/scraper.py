#!/bin/env python3
# Modified by @botkillerme
# Telegram Group: http://t.me/botkillerme
# Please give me credits if you use any codes from here.



from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import os, sys
import configparser
import csv
import time

re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
yo="\033[1;33m"

def banner():
    print(f"""
byHürKöle
        """)

cpass = configparser.RawConfigParser()
cpass.read('config.data')

try:
    api_id = cpass['cred']['id']
    api_hash = cpass['cred']['hash']
    phone = cpass['cred']['phone']
    client = TelegramClient(phone, api_id, api_hash)
except KeyError:
    os.system('clear')
    banner()
    print("python setup.py Çalıştırınız [!]\n")
    sys.exit(1)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    os.system('clear')
    banner()
    client.sign_in(phone, input(gr+'[+] Telegramdan Gelen KOD : '+yo))

os.system('clear')
banner()
chats = []
last_date = None
chunk_size = 200
groups=[]

result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup== True:
            groups.append(chat)
    except:
        continue

print(gr+'[+] Hesabınızdaki Gruplar '+re)
for i, g in enumerate(groups):
    print(gr+'['+cy+str(i)+']' + ' - ' + g.title)
print('')
g_index = input(gr+"[+] Üyelerini Kaydetmek İstediğin Grup  :  "+re)
target_group=groups[int(g_index)]

print(gr+'[+] Bekleyiniz ...')
time.sleep(1)
all_participants = []
all_participants = client.iter_participants(target_group)

print(gr+'[+] Kaydedildi ...')
time.sleep(1)
with open("members.csv","w",encoding='UTF-8') as f:
    writer = csv.writer(f,delimiter=",",lineterminator="\n")
    writer.writerow(['username','user id', 'access hash','name','group', 'group id'])
    for user in all_participants:
        username = user.username or ""
        first_name = user.first_name or ""
        last_name = user.last_name or ""
        name= (first_name + ' ' + last_name).strip()
        writer.writerow([username,user.id,user.access_hash,name,target_group.title, target_group.id])
print(gr+'[+] Başarıyla Tamamlandı!')
