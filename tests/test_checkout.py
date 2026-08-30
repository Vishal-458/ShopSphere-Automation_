from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import pytest


@pytest.mark.smoke
@pytest.mark.ui
@pytest.mark.regression
def test_complete_order(
    login_page,
    home_page,
    product_page,
    cart_page,
    checkout_page,
    test_data
):

    login_page.open()

    login_page.login(
        test_data["valid_user"]["username"],
        test_data["valid_user"]["password"]
    )

    home_page.open_product("Sauce Labs Backpack")

    product_page.add_to_cart()

    cart_page.open()

    assert cart_page.get_item_count() == 1

    cart_page.checkout()

    checkout_page.enter_customer_information(
        test_data["customer"]["first_name"],
        test_data["customer"]["last_name"],
        test_data["customer"]["postal_code"]
    )

    checkout_page.continue_to_overview()

    assert checkout_page.get_page_title() == "Checkout: Overview"

    checkout_page.finish_order()

    assert checkout_page.get_order_confirmation() == "Thank you for your order!"
def test_checkout_without_customer_information(
    login_page,
    home_page,
    product_page,
    cart_page,
    checkout_page,
    test_data
):

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    home_page.open_product(test_data["products"]["backpack"])

    product_page.add_to_cart()

    cart_page.open()

    cart_page.checkout()

    checkout_page.continue_to_overview()

    assert checkout_page.page.locator(
        "[data-test='error']"
    ).is_visible()