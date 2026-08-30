from playwright.sync_api import Locator, Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)

    def click(self, locator: Locator):
        locator.click()

    def fill(self, locator: Locator, text: str):
        locator.fill(text)

    def get_text(self, locator: Locator) -> str:
        return locator.inner_text()

    def is_visible(self, locator: Locator) -> bool:
        return locator.is_visible()