import pytest
from src.widget import mask_account_card, get_date

@pytest.mark.parametrize(
    "number, masked_number",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 12345678909876554356", "Счет **4356")
    ],
)
def test_mask_account_card_different(number, masked_number):
    assert mask_account_card(number) == masked_number

def test_get_date(date_string):
    assert get_date(date_string) == "11.03.2024"


def test_get_date_wrong(wrong_date_string):
    assert get_date(wrong_date_string) == ""