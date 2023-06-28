from src.phone import Phone
import pytest


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_repr_phone(phone):
    assert phone.__repr__() == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim(phone):
    phone.number_of_sim = 1
    assert phone.number_of_sim == 1
    with pytest.raises(ValueError):
        phone.number_of_sim = -1
