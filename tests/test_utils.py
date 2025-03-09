import os

import pytest

from src.utils import get_transactions


@pytest.mark.parametrize(
    "path, expected",
    [
        (
            os.path.abspath("../data/test_operation.json"),
            [
                {
                    "id": 441945886,
                    "state": "EXECUTED",
                    "date": "2019-08-26T10:50:58.294041",
                    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Maestro 1596837868705199",
                    "to": "Счет 64686473678894779589",
                }
            ],
        ),
        ("test_operation.json", []),
        (os.path.abspath("../data/test_operation_wrong.json"), []),
    ],
)
def test_get_transactions(path, expected):
    assert get_transactions(path) == expected
