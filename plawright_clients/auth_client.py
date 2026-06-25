from plawright_clients.base_client import BaseClient


class AuthClient(BaseClient):

    def auth(self, email: str, password: str):
        response = self._post(url="api/ecom/auth/login",
                              data={"userEmail": email,
                                    "userPassword": password})
        if not response.ok:
            raise ValueError(f"Login failed with status code {response.status_code}")
        return response.json()["token"]
