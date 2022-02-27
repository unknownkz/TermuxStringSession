# Copyleft (c) 2021 unknownkz, All wrongs reserved.
#
# Redistribution and use in source with or
# without modufication, are permitted.


import time

from pyrogram import Client
from telethon.sessions import StringSession
from telethon.sync import TelegramClient

select = " "

docs = """Generate your Telegram String Session
pyro -->> Pyrogram [https://docs.pyrogram.org]
tele -->> Telethon [https://docs.telethon.dev]
"""

tutor = """
~ go-to my.telegram.org
~ Login using your Telegram account
~ Click on API Development Tools
~ Create a new application, by entering the required details
~ Check your Telegram saved messages section to copy the STRING_SESSION
"""

template = """
Thank you guys...
Manage by @GroupTidakDiketahui
            
<code>STRING_SESSION</code>: <code>{}</code>
⚠️ <b>Please be carefull to pass this value to third parties</b>"""


print(docs)

while select != ("pyro", "tele"):
    select = input("Enter your required client < pyro / tele > : ").lower()
    if select == "tele":
        print("""\nTelethon selected\nRunning script...""")
        time.sleep(1)
        print(tutor)
        API_KEY = int(input("Enter API_KEY here: "))
        API_HASH = input("Enter API_HASH here: ")

        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
            session_string = client.session.save()
            saved_messages_template = "Telethon session" + template.format(
                session_string
            )
            print("\nGenerating String Session...\n")
            client.send_message("me", saved_messages_template, parse_mode="html")
            time.sleep(1)
            print(
                "Your STRING_SESSION value have been sent to your Telegram Saved Messages"
            )
        break

    elif select == "pyro":
        print("""\nPyrogram selected.\nRunning script...""")
        time.sleep(1)
        print(tutor)
        API_ID = int(input("Enter API_ID here: "))
        API_HASH = input("Enter API_HASH here: ")

        with Client(":memory:", api_id=API_ID, api_hash=API_HASH) as pyro:
            saved_messages_template = "Pyrogram session" + template.format(
                pyro.export_session_string()
            )
            print("\nGenerating String session...\n")
            pyro.send_message("me", saved_messages_template, parse_mode="html")
            time.sleep(1)
            print(
                "Your STRING_SESSION value have been sent to your Telegram Saved Messages"
            )
        break

    else:
        print("\nPlease only select pyro or tele\n")
        time.sleep(1.5)
