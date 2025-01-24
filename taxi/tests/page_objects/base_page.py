from playwright.sync_api import Page
from .locators.locators import Locators
from typing import Any


class BasePage:
    PAGE_NAME = None
    ADD_LINK = None

    def __init__(self, page: Page) -> None:
        self.page = page
        self.link = self.page.get_by_role(Locators.LINK, name=self.PAGE_NAME)
        self.button = self.page.get_by_role(Locators.BUTTON, name=self.PAGE_NAME)

    def click_on_link(self) -> None:
        self.link.click()

    def click_on_button(self) -> None:
        self.button.click()

    def is_element_exist(self, text: str, role: str) -> Any:
        element = self.page.locator(f"//{role}[contains(text(), '{text}')]")

        return element.is_visible()

    def click_on_link_with_name(self, name: str) -> None:
        link = self.page.get_by_role("link", name=name)

        link.click()

    def fill_the_field_with_text(self, field: str, text: str) -> None:
        input_field = self.page.get_by_label(field)

        input_field.click()
        input_field.fill(text)

    def click_on_button_with_name(self, name: str) -> None:
        button = self.page.get_by_role("button", name=name)

        button.click()

    def select_dropdown_option(self, dropdown_label: str, option: str) -> None:
        dropdown_object = self.page.get_by_label(dropdown_label)

        dropdown_object.select_option(option)

    def check_checkbox(self, checkbox_label: str) -> None:
        checkbox_object = self.page.get_by_label(checkbox_label)

        checkbox_object.check()
        checkbox_object.is_checked()

    def click_on_object_update_button(self, object_attribs: str) -> None:
        object_attribs = object_attribs.split()
        object_xpath = Locators.USER_WITH_PROPERTIES.format(*object_attribs)
        update_button_xpath = object_xpath + Locators.UPDATE_BUTTON

        self.page.click(update_button_xpath)

    def click_on_object_delete_button(self, object_attribs: str) -> None:
        object_attribs = object_attribs.split()
        object_xpath = Locators.USER_WITH_PROPERTIES.format(*object_attribs)
        delete_button_xpath = object_xpath + Locators.DELETE_BUTTON

        self.page.click(delete_button_xpath)
