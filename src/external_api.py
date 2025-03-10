import os

import requests
from dotenv import load_dotenv


def get_transaction_amount(transaction):
    """Возвращает сумму транзакции в рублях"""
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        amount = transaction["operationAmount"]["amount"]
        return float(amount)
    elif (
        transaction["operationAmount"]["currency"]["code"] == "USD"
        or transaction["operationAmount"]["currency"]["code"] == "EUR"
    ):
        load_dotenv()
        headers = {"apikey": os.getenv("API_KEY")}
        response = requests.get(
            f"https://api.apilayer.com/exchangerates_data/convert"
            f"?to=RUB&from={transaction['operationAmount']['currency']['code']}"
            f"&amount={transaction['operationAmount']['amount']}",
            headers,
        )

        content = response.json()
        result = content["result"]
        return result


if __name__ == "__main__":

    print(
        get_transaction_amount(
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        )
    )
