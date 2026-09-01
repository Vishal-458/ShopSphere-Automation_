import pytest

from utils.test_data_reader import load_test_data


LOGIN_USERS = load_test_data()["login_users"]


@pytest.mark.smoke
@pytest.mark.ui
def test_valid_login(login_page, test_data):

    login_page.open()

    login_page.login(
        test_data["valid_user"]["username"],
        test_data["valid_user"]["password"]
    )

    assert "inventory" in login_page.page.url


@pytest.mark.ui
@pytest.mark.regression
@pytest.mark.parametrize(
    "login_data",
    LOGIN_USERS,
    ids=[
        "standard_user",
        "locked_out_user",
        "invalid_user"
    ]
)
def test_login_with_multiple_users(
    login_page,
    home_page,
    login_data
):

    login_page.open()

    login_page.login(
        login_data["username"],
        login_data["password"]
    )

    if login_data["expected_success"]:
        assert home_page.get_page_title() == "Products"

    else:
        assert login_page.get_error_message() != ""