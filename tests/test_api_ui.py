import pytest


@pytest.mark.ui
@pytest.mark.api
def test_api_data_can_be_used_with_ui(
    api_client,
    login_page,
    home_page,
    test_data
):

    payload = test_data["api"]["post"]

    response = api_client.create_resource(
        "/posts",
        payload
    )

    assert response.status_code == 201

    api_data = response.json()

    assert api_data["title"] == payload["title"]
    assert api_data["userId"] == payload["userId"]

    login_page.open()

    login_page.login(
        test_data["valid_user"]["username"],
        test_data["valid_user"]["password"]
    )

    assert home_page.get_page_title() == "Products"