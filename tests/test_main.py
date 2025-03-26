import builtins

import pytest
import unittest
from unittest.mock import patch


from config import DATA_DIR
import os
from main import main


@patch("builtins.input", side_effect=[1, "CANCELED", "да", "по возрастанию", "да", "да", "Перевод организации"])
def test_main(mock_input):
    result = main()
    assert result == "Успешно"
