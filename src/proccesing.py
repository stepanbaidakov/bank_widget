from typing import Optional, Any, List, Dict


def filter_by_state(list_dictionary: List[Dict[str, Any]], state: Optional[str] = "EXECUTED") -> List[Dict[str, Any]]:
    """Возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному
    значению."""
    new_list = []
    for dictionary in list_dictionary:
        if dictionary.get("state") == state:
            new_list.append(dictionary)
    return new_list


def sort_by_date(list_dictionary: List[dict[str, Optional[str]]], sorting: bool = True) -> List[Dict[str, Any]] :
    """Возвращает новый список отсортированный по дате"""
    sorted_list = sorted(list_dictionary, key =lambda item: item.get("date", ""), reverse=sorting)
    return sorted_list
