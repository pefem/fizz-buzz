import pytest


@pytest.fixture()
def valid_entries():
    return ("3", "5")


@pytest.fixture()
def invalid_entries():
    return ("3", "bad_entry")
