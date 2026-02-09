import requests
from bs4 import BeautifulSoup
import logging
import time

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# URL страницы с цитатами
URL = "https://quotes.toscrape.com/"

def fetch_quote():
    response = requests.get(URL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quote = soup.find(class_='quote')
        if quote:
            text = quote.find(class_='text').text.strip()
            author = quote.find(class_='author').text.strip()
            logging.info(f'{text} - {author}')
        else:
            logging.info("Цитаты не найдены")
    else:
        logging.error(f"Ошибка при запросе: {response.status_code}")

# Запуск бесконечного цикла
while True:
    fetch_quote()
    time.sleep(10)  # Ожидание 10 секунд перед следующим запросом
