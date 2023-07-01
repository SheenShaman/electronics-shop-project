from src.item import Item


class MixinLang:

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'
        return self


class Keyboard(Item, MixinLang):
    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        self._language = language

    @property
    def language(self):
        return self._language
