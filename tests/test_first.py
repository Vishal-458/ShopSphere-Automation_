import pytest

pytestmark = pytest.mark.ui
from playwright.sync_api import Page

@pytest.mark.ui
def test_open_website(page: Page):

    page.goto("https://www.saucedemo.com/")

    print(page.title())

    assert "Swag Labs" in page.title()