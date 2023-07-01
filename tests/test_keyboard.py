from src.keyboard import Keyboard
import pytest


@pytest.fixture
def keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_str(keyboard):
    assert str(keyboard) == "Dark Project KD87A"


def test_str_language(keyboard):
    assert str(keyboard.language) == "EN"


def test_change_lang(keyboard):
    keyboard.change_lang()
    assert str(keyboard.language) == "RU"
    keyboard.change_lang().change_lang()
    assert str(keyboard.language) == "RU"


def test__attribute_error(keyboard):
    with pytest.raises(AttributeError):
        keyboard.language = 'CH'
