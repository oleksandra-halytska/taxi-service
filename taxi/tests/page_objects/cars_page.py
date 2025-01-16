from playwright.sync_api import Page, expect
from .locators.locators import Locators


class CarsPage:
    def __init__(self, page) -> None:
        self.page = page
        self.link = self.page.get_by_role(Locators.LINK, name="All cars")

    def click_on_link(self) -> None:
        self.link.click()

    def is_car_list_exists(self, text: str) -> bool:
        element = self.page.get_by_role('heading', name=text)
        expect(element).to_be_visible()
