import json
from pyrogram import Client
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid,
)
with open("sessions.json","r") as file:
  data = json.load(file)

with open("phones.txt") as file:
  phones = [phone.strip() for phone in file.readlines()]
for phone in phones:
  if not data.get(phone):
    client = Client("kanciyan", 22592549, "1387d57b3c1427ba951b8b7ecd2d235d", in_memory = True)
    print(f"[{phone}] Giriş Yapılıyor...")
    client.connect()
    try:
      code = client.send_code(phone)
    except PhoneNumberInvalid:
      print(f"[{phone}] Telefon Numarası Geçersiz. Lütfen Doğru Formatta Girdiğinizden Emin Olun!")
      break
    codestr = input(f"[{phone}] Telegram Tarafından Gönderilen Kodu Giriniz: ")
    try:
      client.sign_in(phone, code.phone_code_hash, codestr)
    except PhoneCodeExpired:
      print(
            f"[{phone}] Kodun Geçerliliği yitirilmiş, yeniden başlat!",
        )
      break
    except SessionPasswordNeeded:
      password = input(f"[{phone}] İki Adımlı Doğrulama: ")
      try:
        client.check_password(password=password)
      except PasswordHashInvalid:
        print(
                f"[{phone}] Şifre Yanlış!",
            )
        break
    string_session = client.export_session_string()
    data.update({phone: string_session})
    with open("sessions.json", "w") as f:
      json.dump(data, f, indent=2)
    print(f"[{phone}] Giriş Başarılı!")









  else:
    print(f"[{phone}] Numara Zaten Kayıtlı!")
