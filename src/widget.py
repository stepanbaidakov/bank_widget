def mask_account_card(client_info: str) -> str:
    """Обрабатывает информацию о картах и счетах"""
    card_type = ""
    if "Счет" in client_info:
        for letter in client_info:
            if letter.isalpha():
                card_type += letter
        nums_list = []
        for num in client_info:
            if num.isdigit():
                nums_list.append(num)
        card_number = "".join(nums_list)
        masked_account_number = f"**{card_number[-4:]}"
        masked_client_info = f"{card_type} {masked_account_number}"
        return masked_client_info
    else:
        for letter in client_info:
            if letter.isalpha():
                card_type += letter
    nums_list = []
    for num in client_info:
        if num.isdigit():
            nums_list.append(num)
    card_number = "".join(nums_list)
    masked_card_number= f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    masked_client_info = f"{card_type} {masked_card_number}"
    return masked_client_info
print(mask_account_card("Счет 73654108430135874305"))


# def get_date(date):
#      """Орабатывает дату"""
#      correct_date = f"{date[8:10]}.{date[5:7]}.{date[:4]}"
#      return correct_date
# print(get_date("2024-03-11ljasljflajlfjla"))
