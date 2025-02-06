import time
import random
import signal
import sys
from telegram_api import send_command
from utils import generate_random_quantity, generate_random_hold_time, generate_random_delay

# Список токенов для торговли
TOKENS = ["BTC", "ETH", "SOL", "DOGE"]

# Функция для хеджирования
def hedge_positions():
    token = random.choice(TOKENS)  # Случайный выбор токена
    quantity = generate_random_quantity()  # Случайный размер позиции
    hold_time = generate_random_hold_time()  # Случайное время удержания

    # Открытие лонг позиции
    print(f"Открытие лонг позиции: {token}, количество: {quantity}")
    send_command(f"/long {token} {quantity}")

    # Открытие шорт позиции
    print(f"Открытие шорт позиции: {token}, количество: {quantity}")
    send_command(f"/short {token} {quantity}")

    # Удержание позиций
    print(f"Удержание позиций в течение {hold_time} секунд...")
    time.sleep(hold_time)

    # Закрытие позиций
    print(f"Закрытие позиций: {token}")
    send_command(f"/close {token}")

# Обработчик для завершения программы
def exit_handler(signal, frame):
    print("Завершение программы...")
    for token in TOKENS:
        send_command(f"/close {token}")
    sys.exit(0)

# Основной цикл
def main():
    signal.signal(signal.SIGINT, exit_handler)  # Обработка Ctrl+C
    try:
        while True:
            hedge_positions()
            delay = generate_random_delay()  # Случайная задержка между действиями
            print(f"Задержка перед следующим действием: {delay} секунд...")
            time.sleep(delay)
    except KeyboardInterrupt:
        print("Программа завершена.")

if __name__ == "__main__":
    main()