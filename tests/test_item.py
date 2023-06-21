from src.item import Item
import pytest


@pytest.fixture
def coll():
    return Item("Смартфон", 10000, 20)


def test_repr(coll):
    assert coll.__repr__() == 'Item(Смартфон, 10000, 20)'


def test_str(coll):
    assert coll.__str__() == 'Смартфон'


def test_calculate_total_price(coll):
    assert coll.calculate_total_price() == 200000


def test_apply_discount(coll):
    assert coll.apply_discount() is None


def test_name(coll):
    coll.name = 'Смартфон'
    assert coll.name == 'Смартфон'
    coll.name = 'СуперСмартфон'
    assert coll.name == 'СуперСмарт'


def test_instantiate_from_csv(coll):
    coll.instantiate_from_csv()
    assert len(coll.all) == 5


def test_string_to_number(coll):
    assert coll.string_to_number('5') == 5
    assert coll.string_to_number('12.99') == 12
