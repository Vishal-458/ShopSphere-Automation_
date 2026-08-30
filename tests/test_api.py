import pytest

pytestmark = pytest.mark.api

@pytest.mark.api
def test_get_post(api_client):

    response = api_client.get("/posts/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
@pytest.mark.api
def test_create_post(api_client):

    payload = {
        "title": "ShopSphere Test",
        "body": "API automation test",
        "userId": 1
    }

    response = api_client.post(
        "/posts",
        payload
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "ShopSphere Test"
    assert data["userId"] == 1
@pytest.mark.api
def test_update_post(api_client):

    payload = {
        "id": 1,
        "title": "Updated ShopSphere Test",
        "body": "Updated API automation test",
        "userId": 1
    }

    response = api_client.put(
        "/posts/1",
        payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Updated ShopSphere Test"
    assert data["body"] == "Updated API automation test"
@pytest.mark.api
def test_patch_post(api_client):

    payload = {
        "title": "Patched ShopSphere Test"
    }

    response = api_client.patch(
        "/posts/1",
        payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Patched ShopSphere Test"
@pytest.mark.api
def test_delete_post(api_client):

    response = api_client.delete("/posts/1")

    assert response.status_code == 200
@pytest.mark.api
def test_get_non_existing_post(api_client):

    response = api_client.get("/posts/99999")

    assert response.status_code == 404
@pytest.mark.api
def test_get_posts_by_user(api_client):

    response = api_client.get(
        "/posts",
        params={"userId": 1}
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0

    for post in data:
        assert post["userId"] == 1
@pytest.mark.api
def test_api_with_headers(api_client):

    headers = {
        "Content-Type": "application/json"
    }

    response = api_client.get(
        "/posts/1",
        headers=headers
    )

    assert response.status_code == 200
    assert response.headers["Content-Type"].startswith(
        "application/json"
    )