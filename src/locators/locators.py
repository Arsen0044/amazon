from src.locators.button_locators import ButtonLocators
from src.locators.fields_locators import FieldLocators
from src.locators.text_locators import TextLocators


class Locators(ButtonLocators, FieldLocators, TextLocators):

    def __init__(self):
        super().__init__()
