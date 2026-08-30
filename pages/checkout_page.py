from playwright.sync_api import Page

from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")

        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")

        self.page_title = page.locator(".title")
        self.order_confirmation = page.locator(".complete-header")

    def enter_customer_information(
        self,
        first_name: str,
        last_name: str,
        postal_code: str
    ):
        self.fill(self.first_name_input, first_name)
        self.fill(self.last_name_input, last_name)
        self.fill(self.postal_code_input, postal_code)

    def continue_to_overview(self):
        self.click(self.continue_button)

    def finish_order(self):
        self.click(self.finish_button)

    def get_page_title(self) -> str:
        return self.get_text(self.page_title)

    def get_order_confirmation(self) -> str:
        return self.get_text(self.order_confirmation)