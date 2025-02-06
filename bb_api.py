import os
import time
import hmac
import hashlib
import requests
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Конфигурация
BYBIT_API_KEY = os.getenv('BYBIT_API_KEY')
BYBIT_API_SECRET = os.getenv('BYBIT_API_SECRET')
BASE_URL = "https://api.bybit.com"

# Функция для подписи запросов
def sign_request(secret, params):
    query_string = '&'.join([f"{key}={value}" for key, value in sorted(params.items())])
    return hmac.new(secret.encode(), query_string.encode(), hashlib.sha256).hexdigest()

# Функция для отправки запросов к API Bybit
def send_request(method, endpoint, params=None):
    if params is None:
        params = {}
    params['api_key'] = BYBIT_API_KEY
    params['timestamp'] = str(int(time.time() * 1000))
    params['sign'] = sign_request(BYBIT_API_SECRET, params)
    url = f"{BASE_URL}{endpoint}"
    response = requests.request(method, url, params=params)
    return response.json()

# Функция для получения баланса
def get_balance():
    endpoint = "/v2/private/wallet/balance"
    response = send_request("GET", endpoint)
    return response

# Функция для открытия позиции
def open_position(symbol, side, quantity):
    endpoint = "/v2/private/order/create"
    params = {
        'symbol': symbol,
        'side': side,
        'order_type': 'Market',
        'qty': quantity,
        'time_in_force': 'GoodTillCancel'
    }
    response = send_request("POST", endpoint, params)
    return response

# Функция для закрытия позиции
def close_position(symbol):
    endpoint = "/v2/private/order/cancelAll"
    params = {'symbol': symbol}
    response = send_request("POST", endpoint, params)
    return response