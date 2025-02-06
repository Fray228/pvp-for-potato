import os
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Конфигурация
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

# Функция для отправки команды боту
def send_command(command):
    params = {
        'chat_id': CHAT_ID,
        'text': command
    }
    response = requests.post(TELEGRAM_API_URL, params=params)
    return response.json()