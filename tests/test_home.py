from playwright.sync_api import Page
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
@pytest.mark.regression
@pytest.mark.ui
def test_products_page(login_page, home_page):

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    assert home_page.get_page_title() == "Products"
    assert home_page.get_product_count() == 6
@pytest.mark.regression
@pytest.mark.ui
def test_products_are_displayed(login_page, home_page):

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    products = home_page.get_product_names()

    assert len(products) == 6
    assert "Sauce Labs Backpack" in products
    assert "Sauce Labs Bike Light" in products
@pytest.mark.regression
@pytest.mark.ui
def test_sort_products_a_to_z(login_page, home_page):

    login_page.open()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    home_page.sort_products("az")

    products = home_page.get_product_names()

    assert products == sorted(products)