from unittest.mock import Mock, patch

import pytest
import requests

from src.external_api import get_transaction_amount


def test_get_transaction_amount_rub(transaction_rubles):
    assert get_transaction_amount(transaction_rubles) == 31957.58


# def get_transaction_amount(transaction):
#     if transaction["operationAmount"]["currency"]["code"] == "RUB":
#         amount = transaction["operationAmount"]["amount"]
#         return float(amount)
#     elif (
#         transaction["operationAmount"]["currency"]["code"] == "USD"
#         or transaction["operationAmount"]["currency"]["code"] == "EUR"
#     ):
#         headers = {"apikey": "iNriqtj5Chhjx24mCiWW7ArTa56l5n46"}
#         response = requests.get(f"https://api.apilayer.com/exchangerates_data/convert?to={"RUB"}&from={transaction["operationAmount"]["currency"]["code"]}&amount={transaction["operationAmount"]["amount"]}", headers) #data=payload, headers=headers)
#         content = response.json()
#         return type(content["result"])


@patch("requests.get")
def test_get_transaction_amount_usd(mock_get):
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 31957.58},
        "info": {"timestamp": 1741217344, "rate": 90.399577},
        "date": "2025-03-05",
        "result": 2888951.713944,
    }
    assert get_transaction_amount(
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ) == {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 31957.58},
        "info": {"timestamp": 1741217344, "rate": 90.399577},
        "date": "2025-03-05",
        "result": 2888951.713944,
    }
    mock_get.assert_called_once_with(
        f"https://api.apilayer.com/exchangerates_data/convert?to={"RUB"}&from=USD&amount=31957.58",
        {"apikey": "iNriqtj5Chhjx24mCiWW7ArTa56l5n46"},
    )


@patch("requests.get")
def test_get_transactions_amount_eur(mock_get):
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "EUR", "to": "RUB", "amount": 31957.58},
        "info": {"timestamp": 1741217344, "rate": 90.399577},
        "date": "2025-03-05",
        "result": 2888951.713944,
    }
    assert get_transaction_amount(
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ) == {
        "success": True,
        "query": {"from": "EUR", "to": "RUB", "amount": 31957.58},
        "info": {"timestamp": 1741217344, "rate": 90.399577},
        "date": "2025-03-05",
        "result": 2888951.713944,
    }
    mock_get.assert_called_once_with(
        f"https://api.apilayer.com/exchangerates_data/convert?to={"RUB"}&from=EUR&amount=31957.58",
        {"apikey": "iNriqtj5Chhjx24mCiWW7ArTa56l5n46"},
    )
