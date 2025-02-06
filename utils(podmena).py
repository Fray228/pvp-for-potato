import random
import time
from fake_useragent import UserAgent

# Функция для генерации случайного размера позиции
def generate_random_quantity():
    return round(random.uniform(0.001, 0.01), 6)  # Пример для BTC

# Функция для генерации случайного времени удержания
def generate_random_hold_time():
    return random.randint(10, 60)  # В секундах

# Функция для генерации случайной задержки
def generate_random_delay():
    return random.randint(5, 15)  # В секундах

# Функция для подмены User-Agent
def get_random_user_agent():
    ua = UserAgent()
    return ua.random