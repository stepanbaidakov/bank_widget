def get_mask_card_number(card_number: int) -> str:
    """Маскирует номер карты"""
    card_number_str = str(card_number)
    masked_number = f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
    return masked_number


def get_mask_account(account_number: int) -> str:
    """Маскирует номер счета"""
    account_number_str = str(account_number)
    masked_number = f"**{account_number_str[-4:]}"
    return masked_number


masked_card_number = get_mask_card_number(input("Введите номер карты"))
print(masked_card_number)
masked_account = get_mask_account(input("Введите номер cчета"))
print(masked_account)
