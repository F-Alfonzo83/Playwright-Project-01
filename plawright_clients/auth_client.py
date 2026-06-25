from plawright_clients.base_client import BaseClient


class AuthClient(BaseClient):

    def auth(self, email: str, password: str):
        response = self._post(url="api/ecom/auth/login",
                              data={"userEmail": email,
                                    "userPassword": password})
        assert response.ok
        return response.json()["token"]
