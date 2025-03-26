from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(client_info: str) -> [str, None]:
    """Обрабатывает информацию о картах и счетах"""

    if isinstance(client_info, int):
        raise AttributeError

    else:
        splited = client_info.split(" ")
        words = []
        masked_number = ""
        for part in splited:
            if part.isdigit():
                if "Счет" in splited:
                    masked_number = get_mask_account(int(part))
                else:
                    masked_number = get_mask_card_number(int(part))
            elif part.isalpha():
                words.append(part)
        card_type = " ".join(words)
        if not masked_number:
            return None
        masked_client_info = f"{card_type} {masked_number}"
        return masked_client_info


def get_date(date: str) -> str:
    """Обрабатывает дату"""
    if date == "":
        return ""
    elif date[:2] != "20":
        return ""

    else:
        correct_date = f"{date[8:10]}.{date[5:7]}.{date[:4]}"
        return correct_date


if __name__ == "__main__":
    print(mask_account_card(""))
