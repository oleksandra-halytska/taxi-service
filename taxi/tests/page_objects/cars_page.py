from .base_page import BasePage
from .locators.locators import Locators
from ..constants.constants import Constants


class CarsPage(BasePage):
    PAGE_NAME = Constants.CARS_PAGE

    def update_object_with_values(self, updated_attribs: str) -> None:
        model, *_ = updated_attribs.split()

        self.fill_the_field_with_text(Locators.MODEL_LABEL, model)
        self.click_on_button_with_name(Locators.SUBMIT)
