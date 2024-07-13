import configparser

from telethon.sync import TelegramClient

config = configparser.ConfigParser()
config.read("../config.ini")

# Your API credentials
api_id = config['Telegram']['API_ID']
api_hash = config['Telegram']['API_HASH']

# Your phone number
phone_number = config['Telegram']['PHONE_NUMBER']

# Your DC ID and server IP for prod OR test environment
dc_id = config['Telegram']['DC_ID']
dc_server_ip = config['Telegram']['TEST_SERVER_IP']

with TelegramClient(__file__[:-3] + '.session', int(api_id), api_hash) as client:
    client.session.set_dc(dc_id, dc_server_ip, 80)
    client.start(phone_number)
    print(client.get_me())
