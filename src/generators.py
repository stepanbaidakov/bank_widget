def filter_by_currency(transactions: list[dict], currency: str):
    """Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной."""
    found = False
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            found = True
            yield transaction

    if not found:
        raise AttributeError("Операции с заданной валютой не существуют!")


def filter_by_currency_csv(transactions: list[dict], currency: str):
    found = False
    for transaction in transactions:
        if transaction["currency_code"] == currency:
            found = True
            yield transaction

    if not found:
        raise AttributeError("Операций с заданной валютой не существуют!")


def transaction_descriptions(transactions: list[dict]):
    """Возвращает описание каждой операции по очереди"""
    if not transactions:
        yield "Описание отсутствует"
    else:
        for transaction in transactions:
            yield transaction.get("description", "Описание отсутсвует")


def card_number_generator(start_value: int, end_value: int):
    """Генерирует номера карт в задонном диапазоне"""
    for num in range(start_value, end_value + 1):
        number = "0" * (16 - len(str(num))) + str(num)
        card_number = f"{number[:4]} {number[4:8]} {number[8:12]} {number[12:]}"
        yield card_number
