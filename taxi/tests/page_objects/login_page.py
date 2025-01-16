from playwright.sync_api import Page
from .locators.locators import Locators


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.link = self.page.get_by_role(Locators.LINK, name="Login")
        self.button = self.page.get_by_role(Locators.BUTTON, name="Login")
        self.username_label = self.page.get_by_label(Locators.USERNAME_LABEL)
        self.password_label = self.page.get_by_label(Locators.PASSWORD_LABEL)

    def click_on_link(self) -> None:
        self.link.click()

    def fill_username_field(self) -> None:
        self.username_label.click()
        self.username_label.fill("test")

    def fill_password_field(self) -> None:
        self.password_label.click()
        self.password_label.fill("123456")

    def click_on_login_button(self) -> None:
        self.button.click()
