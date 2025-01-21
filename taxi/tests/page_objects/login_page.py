from .locators.locators import Locators
from .base_page import BasePage


class LoginPage(BasePage):
    PAGE_NAME = "Login"

    def __init__(self, page) -> None:
        super().__init__(page)
        self.username_label = self.page.get_by_label(Locators.USERNAME_LABEL)
        self.password_label = self.page.get_by_label(Locators.PASSWORD_LABEL)

    def fill_username_field(self) -> None:
        self.username_label.click()
        self.username_label.fill("test")

    def fill_password_field(self) -> None:
        self.password_label.click()
        self.password_label.fill("123456")
