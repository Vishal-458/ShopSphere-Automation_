from playwright.sync_api import Page

from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.cart_items = page.locator(".cart_item")
        self.item_names = page.locator(".inventory_item_name")
        self.checkout_button = page.locator("#checkout")
        self.continue_shopping_button = page.locator("#continue-shopping")

    def open(self):
        self.page.goto("https://www.saucedemo.com/cart.html")

    def get_item_count(self) -> int:
        return self.cart_items.count()

    def get_item_names(self) -> list[str]:
        return self.item_names.all_inner_texts()

    def checkout(self):
        self.click(self.checkout_button)

    def continue_shopping(self):
        self.click(self.continue_shopping_button)