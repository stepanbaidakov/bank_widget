import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == "7000 79** **** 6361"


@pytest.mark.parametrize(
    "number, masked_card_number",
    [
        ("l;ajf;ljf;lafj;lajf;ajf", "l;aj f;** **** ;ajf"),
        (19084971409719048107497937174010197907510978791087, "1908 49** **** 1087"),
        (8126486, "8126 48** **** 6486"),
    ],
)
def test_get_mask_card_number_different(number, masked_card_number):
    assert get_mask_card_number(number) == masked_card_number


@pytest.mark.parametrize("number, masked_card_number", [("", "")])
def test_get_mask_card_number_empty(number, masked_card_number):
    assert get_mask_card_number(number) == masked_card_number


def test_get_mask_account_number(account_number):
    assert get_mask_account(account_number) == "**4305"


@pytest.mark.parametrize(
    "number, masked_account_number",
    [("ljal;jfl;ajfa;ljf;afypp", "**fypp"), (180768451895619691897913274371979179791797917, "**7917")],
)
def test_get_mask_account_number_different(number, masked_account_number):
    assert get_mask_account(number) == masked_account_number


@pytest.mark.parametrize("number, masked_account_number", [(8147917, "**7917")])
def test_get_mask_account_number_smaller(number, masked_account_number):
    assert get_mask_account(number) == masked_account_number
