from playwright.async_api import Page, expect
from .locators.locators import Locators
from typing import Optional, Any


class BasePage:
    PAGE_NAME = None

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
