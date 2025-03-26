import os

from config import DATA_DIR
from src.generators import filter_by_currency, filter_by_currency_csv
from src.pandas_utils import get_transactions_csv, get_transactions_exel_csv
from src.proccesing import filter_by_state, sort_by_date
from src.utils import find_transactions_by_search, get_transactions
from src.widget import mask_account_card


def main():
    """Отвечает за основную логику проекта и связывает функциональности между собой"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    while True:
        print(
            "Выберите необходимый пункт меню:\n"
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла\n"
        )
        user_input = int(input("Выберите необходимый пункт меню: "))
        if user_input == 1:
            transactions = get_transactions(os.path.join(DATA_DIR, "operations.json"))
            break
        elif user_input == 2:
            transactions = get_transactions_csv(os.path.join(DATA_DIR, "transactions.csv"))
            break
        elif user_input == 3:
            transactions = get_transactions_exel_csv(os.path.join(DATA_DIR, "transactions_excel.xlsx"))
            break
        else:
            print("Такого выбора нету")

    while True:
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )

        user_input = input("Введите статус: ").upper()
        if user_input in ["EXECUTED", "CANCELED", "PENDING"]:
            transactions = filter_by_state(transactions, user_input)
            break
        else:
            print(f"Статус операции {user_input} недоступен.")

    while True:
        print("Отсортировать операции по дате? Да/Нет")
        user_input = input("Ваш ответ: ")
        if user_input.title() == "Да":

            print("Отсортировать по возрастанию или по убыванию?")
            user_input = input("Выберите один из вариантов: ")
            if user_input == "по возрастанию":
                transactions = list(sort_by_date(transactions, False))
                break
            elif user_input == "по убыванию":
                transactions = list(sort_by_date(transactions))
                break
            else:
                print("Введите правильные данные")
        elif user_input.title() == "Нет":
            break
        else:
            print("Введите правильные данные")

    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        user_input = input("Ваш ответ: ")
        if user_input.title().title() == "Да":
            if transactions[0]["operationAmount"]:
                transactions = list(filter_by_currency(transactions, "RUB"))
            else:
                transactions = list(filter_by_currency_csv(transactions, "RUB"))
            break
        elif user_input.title() == "Нет":
            break
        else:
            print("Такого ответа нету")

    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        user_input = input("Ваш ответ: ")
        print()
        if user_input.title() == "Да":
            user_input = input("Введите слово для поиска: ")
            transactions = find_transactions_by_search(transactions, user_input)
            break
        elif user_input.title() == "Нет":
            break
        else:
            print("Такого описания нету")

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return "Нет транзакций"
    else:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(transactions)}")

    for transaction in transactions:

        print(f"\n{transaction.get("date", "")} {transaction.get("description", "")}")
        if transaction.get("from", "") != "":

            print(f"{mask_account_card(str(transaction.get("to", "")))} ->")
            print(f"{mask_account_card(str(transaction.get("from", "")))}")

        else:
            print(mask_account_card(transaction.get("to", "")))

        if "operationAmount" in transaction:
            print(
                f"Сумма: {transaction.get("operationAmount", "").get("amount", "")}"
                f" {transaction.get("operationAmount", "").get("currency", "").get("name", "")}"
            )
        else:
            print(f"Сумма: {transaction.get("amount", "")} {transaction.get("currency_name", "")}")
        return "Успешно"


if __name__ == "__main__":
    main()
