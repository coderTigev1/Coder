from pyrogram import Client, filters, idle
from asyncio.exceptions import TimeoutError
import asyncio
import json
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid,
)
import pyromod.listen
import random
from pyrogram import enums
API_ID = 3197282
API_HASH = "f132d14a0ed82df532405db9001db797"
TOKEN = "6010405236:AAEgaUn5SZnh15mGP9dGjVPFw2IVLHSwFT0"
texts = [
f"Random Mesaj {i}" for i in range(100)
]
bot = Client("kancibot", API_ID, API_HASH, bot_token = TOKEN)
status = False
chats = [
-1001970181039,
-1001665800030,
-1001949686407,
]

@bot.on_message(filters.command("join"))
async def check_and_join(_,m):
  if m.chat.id not in chats:
    return await m.reply("yetkisiz Grup!")
  admin = []
  async for msg in bot.get_chat_members(m.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
    admin.append(msg.user.id)
  if m.from_user.id not in admin:
    return await m.reply("yetkisiz kullanıcı!")
  link = await bot.export_chat_invite_link(m.chat.id)
  with open("sessions.json") as f:
    phones = json.load(f)
  for key in list(phones.keys()):
    async with Client("kanciyan", session_string = phones[key]) as cli:
      await cli.join_chat(link)

@bot.on_message(filters.command("leave"))
async def check_and_leave(_,m):
  if m.chat.id not in chats:
    return await m.reply("yetkisiz Grup!")
  admin = []
  async for msg in bot.get_chat_members(m.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
    admin.append(msg.user.id)
  if m.from_user.id not in admin:
    return await m.reply("yetkisiz kullanıcı!")
  with open("sessions.json") as f:
    phones = json.load(f)
  for key in list(phones.keys()):
    async with Client("kanciyan", session_string = phones[key]) as cli:
      await cli.leave_chat(m.chat.id)

@bot.on_message(filters.command("write"))
async def check_and_write(_,m):
  if m.chat.id not in chats:
    return await m.reply("yetkisiz Grup!")
  global status
  status = True
  admin = []
  async for msg in bot.get_chat_members(m.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
    admin.append(msg.user.id)
  if m.from_user.id not in admin:
    return await m.reply("yetkisiz kullanıcı!")
  while status:
    with open("sessions.json") as f:
      phones = json.load(f)
    for key in list(phones.keys()):
      if not status:
        break
      try:
        async with Client("kanciyan", session_string = phones[key]) as cli:
          await cli.send_message(m.chat.id, random.choice(texts))
      except:
        continue



@bot.on_message(filters.command("cancel"))
async def check_and_close(_,m):
  if m.chat.id not in chats:
    return await m.reply("yetkisiz Grup!")
  global status
  status = False
  admin = []
  async for msg in bot.get_chat_members(m.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
    admin.append(msg.user.id)
  if m.from_user.id not in admin:
    return await m.reply("yetkisiz kullanıcı!")
if __name__ == "__main__":
  bot.start()
  print(bot.get_me().first_name)
  print("aktif")
  idle()
