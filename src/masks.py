import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s %(levelname)s: %(message)s',
                    filename="../logs/.log",
                    filemode='w', encoding="utf-8")
mask_card_number_logger = logging.getLogger("app.mask_card_number")
mask_account_logger = logging.getLogger("app.mask_account")


def get_mask_card_number(card_number: int) -> str:
    """Маскирует номер карты"""

    if card_number != "":
        mask_card_number_logger.info(f"Номер карты маскируется")
        card_number_str = str(card_number)
        masked_number = f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
        return masked_number
    else:
        mask_card_number_logger.warning(f"Номер карты не был указан")
        return ""


def get_mask_account(account_number: int) -> str:
    """Маскирует номер счета"""
    if account_number != "":
        mask_account_logger.info(f"Номер счета маскируется")
        account_number_str = str(account_number)
        masked_number = f"**{account_number_str[-4:]}"
        return masked_number
    else:
        mask_account_logger.warning(f"Номер счета не был указан")
        return ""
