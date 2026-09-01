from playwright.sync_api import Page

from pages.base_page import BasePage
from utils.logger import get_logger


class LoginPage(BasePage):

    logger = get_logger(__name__)

    def __init__(self, page: Page, base_url: str):
        super().__init__(page)

        self.base_url = base_url

        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def open(self):
        self.logger.info("Opening login page")
        self.page.goto(self.base_url)

    def login(self, username: str, password: str):
        self.logger.info(
            f"Attempting login with username: {username}"
        )

        self.username_input.fill(username)
        self.password_input.fill(password)

        self.login_button.click()

        self.logger.info("Login button clicked")
    def get_error_message(self) -> str:
        return self.page.locator(
        "[data-test='error']"
    ).inner_text()