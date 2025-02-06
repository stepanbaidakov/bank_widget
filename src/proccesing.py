from typing import Optional


def filter_by_state(list_dictionary: list[dict], state: Optional[str] = "EXECUTED") -> list[dict]:
    """возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению."""
    new_list = []
    for dictionary in list_dictionary:
        if dictionary["state"] == state:
            new_list.append(dictionary)
    return new_list


def sort_by_date(list_dictionary: list[dict], sorting: bool =True) -> list[dict]:
    """Возващает новый список отсортированный по дате"""
    sorted_list = sorted(list_dictionary, key=lambda date: date.get("date"), reverse=sorting)
    return sorted_list
