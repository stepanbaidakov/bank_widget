import json
import logging
import os

from config import DATA_DIR, LOGS_DIR

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
        transactions_logger.error(f"Указанного пути не существует.")
        return []

    with open(my_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    if isinstance(data, list):
        transactions_logger.info(f"Файл содержит список, трансакции обрабатываются")
        return data
    else:
        transactions_logger.error(f"Файл содержит не список")
        return []


# current_directory = os.getcwd()
# print(current_directory)


# print(get_transactions(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))), "operations.json")
# print(get_transactions("../data/operations.json"))

print(get_transactions(os.path.join(DATA_DIR, "operations.json")))
# print(base_dir)
# print(get_transactions(base_dir))
