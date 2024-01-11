import logging
from login import client
from telethon.tl.functions.account import UpdateStatusRequest
import time
from dotenv import load_dotenv
import os

load_dotenv()
delay = os.getenv("DELAY")

if client.is_user_authorized():
    logging.info("You are now always ONLINE")
    while True:
        result = client(UpdateStatusRequest(offline=False))
        time.sleep(int(delay))
        logging.debug(F"Sleep for {delay} seconds...")
else:
    logging.fatal("Login FAILED! Please, try again.")
