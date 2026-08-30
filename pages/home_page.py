from playwright.sync_api import Page

from pages.base_page import BasePage
from utils.logger import get_logger


class HomePage(BasePage):

    logger = get_logger(__name__)

    def __init__(self, page: Page):
        super().__init__(page)

        self.page_title = page.locator(".title")
        self.product_items = page.locator(".inventory_item")
        self.product_names = page.locator(".inventory_item_name")
        self.sort_dropdown = page.locator(".product_sort_container")

    def get_page_title(self) -> str:
        self.logger.info("Reading products page title")
        return self.get_text(self.page_title)

    def get_product_count(self) -> int:
        self.logger.info("Getting product count")
        return self.product_items.count()

    def get_product_names(self) -> list[str]:
        self.logger.info("Getting product names")
        return self.product_names.all_inner_texts()

    def sort_products(self, option: str):
        self.logger.info(f"Sorting products using option: {option}")
        self.sort_dropdown.select_option(option)

    def open_product(self, product_name: str):
        self.logger.info(f"Opening product: {product_name}")

        product = self.product_items.filter(
            has_text=product_name
        ).locator(".inventory_item_name")

        product.click()