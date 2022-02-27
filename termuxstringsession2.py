# (c) https://t.me/TelethonChat/37677
# This Source Code Form is subject to the terms of the GNU
# General Public License, v.3.0. If a copy of the GPL was not distributed with this
# file, You can obtain one at https://www.gnu.org/licenses/gpl-3.0.en.html.


from telethon.sessions import StringSession
from telethon.sync import TelegramClient


desc = """
Thank you very much for using this script.

<code>STRING_SESSION</code>: <code>{}</code>
⚠️ <b>Please be carefull to pass this value to third parties</b>

Credits : @TelethonUpdates

Managed by : @GroupTidakDiketahui
"""



print(
   """
 /$$   /$$ /$$$$$$$$ /$$   /$$ /$$$$$$$$  /$$$$$$
| $$  /$$/| $$_____/| $$$ | $$|_____ $$  /$$__  $$
| $$ /$$/ | $$      | $$$$| $$     /$$/ | $$  \ $$
| $$$$$/  | $$$$$   | $$ $$ $$    /$$/  | $$  | $$
| $$  $$  | $$__/   | $$  $$$$   /$$/   | $$  | $$
| $$\  $$ | $$      | $$\  $$$  /$$/    | $$  | $$
| $$ \  $$| $$$$$$$$| $$ \  $$ /$$$$$$$$|  $$$$$$/
|__/  \__/|________/|__/  \__/|________/ \______/
"""
)
print("")
print("""Telethon String !!! No Using API_HASH & API_ID""")
print("")
print("")
print("""Credits by : @xelyourslurred <unknownkz>""")
API_KEY = "1273127"
API_HASH = "2626aee4ea587947c6a703f1a0d6a3cc"

while True:
    try:
        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
            print("")
            session = client.session.save()
            messages_temp = desc.format(session)
            client.send_message(
                "me", messages_temp, parse_mode="html"
            )
    except:
        print("")
        print("Wrong phone number!!!\nMake sure it's with correct country code.")
        print("")
        continue
    break
