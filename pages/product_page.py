from playwright.sync_api import Page

from pages.base_page import BasePage


class ProductPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)

        self.product_name = page.locator(".inventory_details_name")
        self.product_price = page.locator(".inventory_details_price")
        self.product_description = page.locator(".inventory_details_desc")
        self.add_to_cart_button = page.locator("#add-to-cart")
        self.back_to_products_button = page.locator("#back-to-products")

    def get_product_name(self) -> str:
        return self.get_text(self.product_name)

    def get_product_price(self) -> str:
        return self.get_text(self.product_price)

    def get_product_description(self) -> str:
        return self.get_text(self.product_description)

    def add_to_cart(self):
        self.click(self.add_to_cart_button)

    def back_to_products(self):
        self.click(self.back_to_products_button)