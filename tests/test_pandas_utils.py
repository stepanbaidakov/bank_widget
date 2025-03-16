
import pytest
from config import DATA_DIR
import os

from src.pandas_utils import get_transactions_csv, get_transactions_exel_csv


@pytest.mark.parametrize(
    "path, expected",
    [
        (
            os.path.join(DATA_DIR, "test_transaction.csv"),
            [
                {
                    "id": 650703,
                    "state": "EXECUTED",
                    "date": "2023-09-05T11:30:32Z",
                    "amount": 16210,
                    "currency_name": "Sol",
                    "currency_code": "PEN",
                    "from": "Счет 58803664561298323391",
                    "to": "Счет 39745660563456619397",
                    "description": "Перевод организации",
                },
                {
                    "id": 3598919,
                    "state": "EXECUTED",
                    "date": "2020-12-06T23:00:58Z",
                    "amount": 29740,
                    "currency_name": "Peso",
                    "currency_code": "COP",
                    "from": "Discover 3172601889670065",
                    "to": "Discover 0720428384694643",
                    "description": "Перевод с карты на карту",
                },
            ],
        ),
        ("test_operation.json", []),
    ],
)
def test_get_transactions_csv(path, expected):
    assert get_transactions_csv(path) == expected


@pytest.mark.parametrize(
    "path, expected",
    [
        ("tests/transactions_excel.xlsx", []),
    ],
)
def test_get_transactions_excel_wrong(path, expected):
    assert get_transactions_csv(path) == expected


transactions = get_transactions_exel_csv(os.path.join(DATA_DIR, "transactions_excel.xlsx"))


def test_get_transaction_excel_correct():
    assert transactions[:3] == [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        },
        {
            "id": 3598919.0,
            "state": "EXECUTED",
            "date": "2020-12-06T23:00:58Z",
            "amount": 29740.0,
            "currency_name": "Peso",
            "currency_code": "COP",
            "from": "Discover 3172601889670065",
            "to": "Discover 0720428384694643",
            "description": "Перевод с карты на карту",
        },
        {
            "id": 593027.0,
            "state": "CANCELED",
            "date": "2023-07-22T05:02:01Z",
            "amount": 30368.0,
            "currency_name": "Shilling",
            "currency_code": "TZS",
            "from": "Visa 1959232722494097",
            "to": "Visa 6804119550473710",
            "description": "Перевод с карты на карту",
        },
    ]


# def test_get_transactions_csv():
#     mock_list = Mock(return_value=os.path.join(DATA_DIR, "transactions_excel.xlsx"))
