from .base_page import BasePage
from .locators.locators import Locators
from ..constants.constants import Constants


class DriversPage(BasePage):
    PAGE_NAME = Constants.DRIVERS_PAGE

    def update_object_with_values(self, updated_attribs: str) -> None:
        license_number, *_ = updated_attribs.split()

        self.fill_the_field_with_text(Locators.LICENSE_LABEL, license_number)
        self.click_on_button_with_name(Locators.UPDATE)
