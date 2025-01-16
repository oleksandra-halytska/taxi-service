from playwright.sync_api import Page
from .locators.locators import Locators


class ManufacturersPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.link = self.page.get_by_role(Locators.LINK, name="All manufacturers")

    def click_on_link(self) -> None:
        self.link.click()
