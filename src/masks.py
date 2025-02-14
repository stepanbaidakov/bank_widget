def get_mask_card_number(card_number: int) -> str:
    """Маскирует номер карты"""
    if card_number != "":
        card_number_str = str(card_number)
        masked_number = f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
        return masked_number
    else:
        return ""


def get_mask_account(account_number: int) -> str:
    """Маскирует номер счета"""
    if account_number != "":
        account_number_str = str(account_number)
        masked_number = f"**{account_number_str[-4:]}"
        return masked_number
    else:
        return ""
