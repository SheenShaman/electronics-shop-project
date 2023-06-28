from src.item import Item
from src.phone import Phone
import pytest


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_repr_item(item):
    assert item.__repr__() == "Item('Смартфон', 10000, 20)"


def test_str_item(item):
    assert item.__str__() == 'Смартфон'


def test_calculate_total_price_item(item):
    assert item.calculate_total_price() == 200000


def test_apply_discount_item(item):
    assert item.apply_discount() is None


def test_name_item(item):
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
    item.name = 'СуперСмартфон'
    assert item.name == 'СуперСмарт'


def test_instantiate_from_csv_item(item):
    item.instantiate_from_csv()
    assert len(item.all) == 5


def test_string_to_number_item(item):
    assert item.string_to_number('5') == 5
    assert item.string_to_number('12.99') == 12


def test_add_item(item, phone):
    assert item + phone == 25
    assert phone + phone == 10
    with pytest.raises(Exception):
        assert item + 2
