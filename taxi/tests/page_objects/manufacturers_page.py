from ..page_objects.base_page import BasePage
from ..page_objects.locators.locators import Locators
from ..constants.constants import Constants


class ManufacturersPage(BasePage):
    PAGE_NAME = Constants.MANUFACTURERS_PAGE

    def update_object_with_values(self, updated_attribs: str) -> None:
        name, country = updated_attribs.split()

        self.fill_the_field_with_text(Locators.NAME_LABEL, name)
        self.fill_the_field_with_text(Locators.COUNTRY_LABEL, country)
        self.click_on_button_with_name(Locators.SUBMIT)
