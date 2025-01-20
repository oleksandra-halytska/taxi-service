from playwright.async_api import Page, expect
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
