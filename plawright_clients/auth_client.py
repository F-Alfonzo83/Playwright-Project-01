from playwright.sync_api import Playwright
from configurations.config import Config
from plawright_clients.base_client import BaseClient

config = Config()
email, password = config.get_credentials_main()

class AuthClient(BaseClient):
    def __init__(self, playwright:Playwright):

        super().__init__(playwright)

    def auth(self, email:str, password:str):
        response = self._post(url="api/ecom/auth/login",
                              data={"userEmail": email,
                                    "userPassword": password })
        assert response.ok
        return response.json()["token"]