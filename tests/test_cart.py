from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

import pytest

pytestmark = pytest.mark.ui
def test_add_product_to_cart(
    login_page,
    home_page,
    product_page,
    cart_page
):

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    home_page.open_product("Sauce Labs Backpack")

    product_page.add_to_cart()

    cart_page.open()

    assert cart_page.get_item_count() == 1

    assert "Sauce Labs Backpack" in cart_page.get_item_names()

def test_add_multiple_products_to_cart(
    login_page,
    home_page,
    product_page,
    cart_page
):

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    home_page.open_product("Sauce Labs Backpack")

    product_page.add_to_cart()

    product_page.back_to_products()

    home_page.open_product("Sauce Labs Bike Light")

    product_page.add_to_cart()

    cart_page.open()

    assert cart_page.get_item_count() == 2

    item_names = cart_page.get_item_names()

    assert "Sauce Labs Backpack" in item_names
    assert "Sauce Labs Bike Light" in item_names