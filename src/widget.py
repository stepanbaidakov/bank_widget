from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(client_info: str) -> str:
    """Обрабатывает информацию о картах и счетах"""
    splited = client_info.split(" ")
    words = []
    for part in splited:
        if part.isdigit():
            if "Счет" in splited:
                    masked_number = get_mask_account(part)
            else:
                    masked_number = get_mask_card_number(part)
        if part.isalpha():
                words.append(part)
    card_type = " ".join(words)
    masked_client_info = f"{card_type} {masked_number}"
    return masked_client_info

print(mask_account_card("Счет 73654108430135874305"))

def get_date(date):
     """Орабатывает дату"""
     correct_date = f"{date[8:10]}.{date[5:7]}.{date[:4]}"
     return correct_date

print(get_date("2023-12-11ljasljflajlfjla"))



# def masked_account_card(client_info: str):
#     splited = client_info.split(" ")
#     words = []
#     for part in splited:
#         if part.isdigit():
#             if "Счет" in splited:
#                 masked_account_number = f"**{part[-4:]}"
#                 masked_number = masked_account_number
#             else:
#                 masked_card_number= f"{part[:4]} {part[4:6]}** **** {part[-4:]}"
#                 masked_number = masked_card_number
#         if part.isalpha():
#             words.append(part)
#     card_type = " ".join(words)
#     masked_client_info = f"{card_type} {masked_number}"
#     return masked_client_info
#
# print(masked_account_card("Счет 35383033474447895560"))
