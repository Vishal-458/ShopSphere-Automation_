import requests


class APIClient:

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()

    def set_auth_token(self, token: str):
        self.session.headers.update({
            "Authorization": f"Bearer {token}"
        })

    def get(self, endpoint: str, params=None, headers=None):
        return self.session.get(
            f"{self.base_url}{endpoint}",
            params=params,
            headers=headers
        )

    def post(self, endpoint: str, data: dict, headers=None):
        return self.session.post(
            f"{self.base_url}{endpoint}",
            json=data,
            headers=headers
        )

    def put(self, endpoint: str, data: dict, headers=None):
        return self.session.put(
            f"{self.base_url}{endpoint}",
            json=data,
            headers=headers
        )

    def patch(self, endpoint: str, data: dict, headers=None):
        return self.session.patch(
            f"{self.base_url}{endpoint}",
            json=data,
            headers=headers
        )

    def delete(self, endpoint: str, headers=None):
        return self.session.delete(
            f"{self.base_url}{endpoint}",
            headers=headers
        )

    def create_resource(self, endpoint: str, data: dict, headers=None):
        response = self.post(
            endpoint,
            data,
            headers=headers
    )
        return response