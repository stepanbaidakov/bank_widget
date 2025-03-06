
from dotenv import load_dotenv
import os
import requests

def get_transaction_amount(transaction):
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        amount = transaction["operationAmount"]["amount"]
        return float(amount)
    elif (
        transaction["operationAmount"]["currency"]["code"] == "USD"
        or transaction["operationAmount"]["currency"]["code"] == "EUR"
    ):
        load_dotenv()
        headers = {"apikey": os.getenv("API_KEY")}
        response = requests.get(f"https://api.apilayer.com/exchangerates_data/convert?to={"RUB"}&from={transaction["operationAmount"]["currency"]["code"]}&amount={transaction["operationAmount"]["amount"]}", headers)
        content =  response.json()
        return content


print(get_transaction_amount({
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }))