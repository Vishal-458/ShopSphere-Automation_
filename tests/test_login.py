import pytest


@pytest.mark.smoke
@pytest.mark.ui
def test_valid_login(login_page, test_data):

    login_page.open()

    login_page.login(
        test_data["valid_user"]["username"],
        test_data["valid_user"]["password"]
    )

    assert "inventory" in login_page.page.url