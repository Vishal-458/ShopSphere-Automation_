from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

import pytest

pytestmark = pytest.mark.ui
def test_product_details(
    login_page,
    home_page,
    product_page,
    test_data
):

    login_page.open()

    login_page.login(
        test_data["valid_user"]["username"],
        test_data["valid_user"]["password"]
    )

    home_page.open_product(
        test_data["products"]["backpack"]
    )

    assert product_page.get_product_name() == \
        test_data["products"]["backpack"]

    assert product_page.get_product_price() == "$29.99"

    assert product_page.get_product_description() != ""

    product_page.add_to_cart()