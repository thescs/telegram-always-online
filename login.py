from telethon import TelegramClient
import logging
import getpass
from dotenv import load_dotenv
import os

load_dotenv()

logging.basicConfig(level=logging.INFO)

if os.getenv("API_ID") == '' or os.getenv("API_HASH") == '':
    logging.fatal("You must assign a API credentials in .env file!")

logging.info("Signing in...")
client = TelegramClient('session_file', os.getenv("API_ID"), os.getenv("API_HASH"), spawn_read_thread=False)

client.connect()
if client.is_user_authorized() is not True:
    logging.info('You is not logged in, trying to log us in using current session...')
    logging.info(
        'If you have 2FA password, please enter right now. This Password will not be stored.')
    password = getpass.getpass()
    if password != '':
        client.start(password=password)
    else:
        client.start()
