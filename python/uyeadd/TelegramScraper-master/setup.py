# -*- coding: utf-8 -*-
#!/bin/env python3
# Modified by @AbirHasan2005
# Telegram Group: http://t.me/linux_repo
# Please give me credits if you use any codes from here.


import os, sys
import configparser
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
def banner():
	os.system('clear')
	print(f"""
{re}.-. . . .-. .-. .   .-. .-. 
{re}|-|  |  |-| |(  |   |-| |(  
{re}` '  `  ` ' ' ' `-' ` ' ' ' 
                            
	""")
banner()
print(gr+"[+] Bekleyiniz ...")
os.system('python3 -m pip install telethon')
os.system('pip3 install telethon')
banner()
os.system("touch config.data")
cpass = configparser.RawConfigParser()
cpass.add_section('cred')
xid = input(gr+"[+] API_ID : "+re)
cpass.set('cred', 'id', xid)
xhash = input(gr+"[+] API_HASH : "+re)
cpass.set('cred', 'hash', xhash)
xphone = input(gr+"[+] Numaranızı Giriniz : "+re)
cpass.set('cred', 'phone', xphone)
with open('config.data', 'w') as setup:
	cpass.write(setup)
print(gr+"[+] Başarıyla Tamamlandı! !")
print('Yazılım Sahibi : https://t.me/botkillerme')
