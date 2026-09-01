import pytest
from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utils.test_data_reader import load_test_data
from utils.config_reader import load_config
from utils.api_client import APIClient
from utils.db_helper import DBHelper

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Environment to run tests against"
    )

@pytest.fixture
def login_page(page: Page, config):
    return LoginPage(
        page,
        config["base_url"]
    )


@pytest.fixture
def home_page(page: Page):
    return HomePage(page)


@pytest.fixture
def product_page(page: Page):
    return ProductPage(page)


@pytest.fixture
def cart_page(page: Page):
    return CartPage(page)


@pytest.fixture
def checkout_page(page: Page):
    return CheckoutPage(page)

@pytest.fixture
def test_data():
    return load_test_data()

@pytest.fixture
def config(request):
    environment = request.config.getoption("--env")
    return load_config(environment)
@pytest.fixture
def api_client(config):
    return APIClient(
        config["api_base_url"]
    )
@pytest.fixture
def db(config):

    db_helper = DBHelper(
        config["database_path"]
    )

    db_helper.connect()

    yield db_helper

    db_helper.close()

@pytest.fixture
def setup_orders_table(db):

    db.execute_update("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY,
            customer_name TEXT NOT NULL,
            product_name TEXT NOT NULL,
            amount REAL NOT NULL,
            status TEXT NOT NULL
        )
    """)

    db.execute_update(
        "DELETE FROM orders"
    )

    yield db

    db.execute_update(
        "DELETE FROM orders"
    )

@pytest.fixture
def setup_shop_tables(db):

    db.execute_update("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    db.execute_update("""
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)

    db.execute_update("""
        CREATE TABLE IF NOT EXISTS shop_orders (
            order_id INTEGER PRIMARY KEY,
            customer_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY(customer_id)
                REFERENCES customers(customer_id),
            FOREIGN KEY(product_id)
                REFERENCES products(product_id)
        )
    """)

    db.execute_update("DELETE FROM shop_orders")
    db.execute_update("DELETE FROM customers")
    db.execute_update("DELETE FROM products")

    yield db

    db.execute_update("DELETE FROM shop_orders")
    db.execute_update("DELETE FROM customers")
    db.execute_update("DELETE FROM products")

