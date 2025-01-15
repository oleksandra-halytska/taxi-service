from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.login_link = self.page.get_by_role("link", name="Login")
        self.login_button = self.page.get_by_role("button", name="Login")
        self.username_label = self.page.get_by_label("Username:")
        self.password_label = self.page.get_by_label("Password:")

    def click_on_login_link(self) -> None:
        self.login_link.click()

    def fill_username_field(self) -> None:
        self.username_label.click()
        self.username_label.fill("test")

    def fill_password_field(self) -> None:
        self.password_label.click()
        self.password_label.fill("123456")

    def click_on_login_button(self) -> None:
        self.login_button.click()
