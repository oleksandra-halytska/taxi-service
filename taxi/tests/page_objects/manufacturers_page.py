from ..page_objects.base_page import BasePage
from ..page_objects.locators.locators import Locators
from ..constants.constants import Constants


class ManufacturersPage(BasePage):
    PAGE_NAME = Constants.MANUFACTURERS_PAGE

    def click_on_object_update_button(self, object_attribs: str) -> None:
        outdated_name, outdated_country = object_attribs.split()
        object_xpath = Locators.USER_WITH_NAME_COUNTRY.format(
            outdated_name, outdated_country
        )
        update_button_xpath = object_xpath + Locators.UPDATE_BUTTON

        self.page.click(update_button_xpath)

    def update_object_with_values(self, updated_attribs: str) -> None:
        name, country = updated_attribs.split()

        self.fill_the_field_with_text(Locators.NAME_LABEL, name)
        self.fill_the_field_with_text(Locators.COUNTRY_LABEL, country)
        self.click_on_button_with_name(Locators.SUBMIT)

    def click_on_object_delete_button(self, object_attribs: str) -> None:
        outdated_name, outdated_country = object_attribs.split()
        object_xpath = Locators.USER_WITH_NAME_COUNTRY.format(
            outdated_name, outdated_country
        )
        delete_button_xpath = object_xpath + Locators.DELETE_BUTTON

        self.page.click(delete_button_xpath)
