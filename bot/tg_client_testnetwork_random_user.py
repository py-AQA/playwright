import configparser
from random import randint
from telethon import TelegramClient, sync
from telethon.errors import PhoneNumberUnoccupiedError, SessionPasswordNeededError

config = configparser.ConfigParser()
config.read("../config.ini")

# TG desktop id & hash
api_id = 17349
api_hash = "344583e45741c457fe1862106095a5eb"

dc_id = config['Telegram']['DC_ID']
client = TelegramClient(None, api_id, api_hash)
client.session.set_dc(dc_id, config['Telegram']['TEST_SERVER_IP'], 80)

client.connect()

# loop for a registered test user without 2FA
while True:
    phone = '+99966' + str(dc_id) + str(randint(0, 9999)).zfill(4)
    client.send_code_request(phone)
    try:
        client.sign_in(phone, str(dc_id) * 5)
    except (PhoneNumberUnoccupiedError, SessionPasswordNeededError):
        continue
    break

print(phone)
print(client.get_me())


async def main():
    async with client.conversation("@qa_testnetwork", timeout=55) as conv:
        await conv.send_message("my phone number is " + phone)
        resp = await conv.get_response()
        print(resp)


if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())
