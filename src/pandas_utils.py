import pandas as pd
import os
import logging
from config import LOGS_DIR

log_path = os.path.join(LOGS_DIR, "utils.log")
transactions_logger = logging.Logger(__name__)
file_handler = logging.FileHandler(log_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
transactions_logger.addHandler(file_handler)
transactions_logger.setLevel(logging.DEBUG)


def get_transactions_csv(path):
    if not os.path.exists(path):
        transactions_logger.error("Указанного пути не существует.")
        return []

    transactions = []

    with open(path, "r", encoding="utf-8"):

        df = pd.read_csv(path, delimiter=";")
    for x, row in df.iterrows():
        transactions.append(dict(row))
    return transactions


def get_transactions_exel_csv(path):
    if not os.path.exists(path):
        transactions_logger.error("Указанного пути не существует.")
        return []

    transactions = []

    df = pd.read_excel(path)
    for x, row in df.iterrows():
        transactions.append(dict(row))
    return transactions
