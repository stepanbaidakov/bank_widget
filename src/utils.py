import json
import os
import requests
from click.core import batch

def get_transactions(path: str) -> list[dict]:
    # path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'operations.json'))
    # print(f"Trying to open file: {path}")
    #
    # if os.path.isdir(path):
    #     print("Error: The path points to a directory, not a file.")
    # else:
    #     with open(path, "r") as file:
    #         data = json.load(file)
    #         return data
    #
    # if not os.path.exists(path):
    #     return []

    with open(path, "w") as file:
        data = json.load(file)
    if isinstance(data, list):
        return data
    else:
        return []


# current_directory = os.getcwd()
# print(current_directory)

# print(get_transactions("operations.json"))
print(get_transactions(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))), "operations.json")
# with open(os.path.join(os.path.dirname(__file__))) as file:
#     data = json.load(file)
# base_path
# print(os.path.dirname(__file__))
# print(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# print(os.access(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')), os.W_OK))