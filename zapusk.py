import time
import signal
import sys
from bybit_api import open_position, close_position, get_balance
from utils import generate_random_quantity, generate_random_hold_time, generate_random_delay

# Список токенов для торговли
TOKENS = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "DOGEUSDT"]

# Функция для хеджирования
def hedge_positions():
    token = random.choice(TOKENS)  # Случайный выбор токена
    quantity = generate_random_quantity()  # Случайный размер позиции
    hold_time = generate_random_hold_time()  # Случайное время удержания

    # Открытие лонг и шорт позиций
    print(f"Открытие лонг позиции: {token}, количество: {quantity}")
    open_position(token, "Buy", quantity)

    print(f"Открытие шорт позиции: {token}, количество: {quantity}")
    open_position(token, "Sell", quantity)

    # Удержание позиций
    print(f"Удержание позиций в течение {hold_time} секунд...")
    time.sleep(hold_time)

    # Закрытие позиций
    print(f"Закрытие позиций: {token}")
    close_position(token)

# Обработчик для завершения программы
def exit_handler(signal, frame):
    print("Завершение программы...")
    for token in TOKENS:
        close_position(token)
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