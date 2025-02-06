from typing import Optional


def filter_by_state(list: list[dict], state: Optional[str]="EXECUTED") -> list[dict]:
    """возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному значению."""
    new_list = []
    for dictionary in list:
        if dictionary["state"] == state:
            new_list.append(dictionary)
    return new_list

print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))

def sort_by_date(list, sorting=True):
    """Возващает новый список отсортированный по дате"""
    sorted_list = sorted(list, key=lambda dictionary: dictionary.get("date"), reverse=sorting)
    return sorted_list

print([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}], False)