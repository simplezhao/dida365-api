from dotenv import load_dotenv
import os
from ticktick.client import TickTickClient
from loguru import logger

load_dotenv()

phone = os.getenv('phone')
password = os.getenv('password')
client = TickTickClient(phone=phone, password=password)


def test_get_token():
    token = client.get_token()
    logger.info(token)
    assert token is not None


def test_get_completed_tasks():
    tasks = client.get_completed_tasks(start_time='2023-11-17 03:37:28', end_time='2023-11-18 03:37:28')
    logger.info(tasks)
    assert tasks is not None
