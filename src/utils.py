import json
import logging
import os
import re
from collections import Counter

from config import LOGS_DIR

log_path = os.path.join(LOGS_DIR, "utils.log")
transactions_logger = logging.Logger(__name__)
file_handler = logging.FileHandler(log_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
transactions_logger.addHandler(file_handler)
transactions_logger.setLevel(logging.DEBUG)


def get_transactions(my_path: str) -> list[dict]:
    """Возвращает список словарей с данными о финансовых транзакциях"""
    if not os.path.exists(my_path):
        transactions_logger.error("Указанного пути не существует.")
        return []

    with open(my_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    if isinstance(data, list):
        transactions_logger.info("Файл содержит список, трансакции обрабатываются")
        return data
    else:
        transactions_logger.error("Файл содержит не список")
        return []


def find_transactions_by_search(transactions_list_dict: list[dict], search_string: str) -> list[dict]:
    """Возвращает список словарей с количеством операций, у которых в описании есть заданная строка в поиске"""
    description_list = []
    if not search_string.strip():  # Проверяем, не пустая ли строка (учитываем пробелы)
        return description_list
    else:
        pattern = re.compile(search_string)
        for transaction in transactions_list_dict:
            if pattern.search(transaction.get("description", "")):
                description_list.append(transaction)

        return description_list


def find_transactions_by_category(transactions_list_dict: list[dict], category_list: list) -> dict:
    """Принимает список с транзакциями и список категорий для поиска и выполняет
поиск всех транзакций в данной категории"""
    result_list = []

    for transaction in transactions_list_dict:
        description = transaction.get("description", "")
        if description in category_list:
            result_list.append(description)

    description_dict = Counter(result_list)
    result_dict = dict(description_dict)
    return result_dict


if __name__ == "__main__":
    # print(get_transactions(os.path.join(DATA_DIR, "operations.json")))
    print(
        find_transactions_by_category(
            [
                {
                    "id": 441945886,
                    "state": "EXECUTED",
                    "date": "2019-08-26T10:50:58.294041",
                    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Maestro 1596837868705199",
                    "to": "Счет 64686473678894779589",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 587085106,
                    "state": "EXECUTED",
                    "date": "2018-03-23T10:45:06.972075",
                    "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Открытие вклада",
                    "to": "Счет 41421565395219882431",
                },
            ],
            ["Перевод организации"],
        )
    )
