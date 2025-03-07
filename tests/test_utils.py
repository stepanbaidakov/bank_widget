import pytest
from unittest.mock import Mock

from src.utils import get_transactions


@pytest.mark.parametrize("path, expected", [("operation.json", [])])
def test_get_transactions(path, expected):
    assert get_transactions(path) == expected