from plawright_clients.base_client import BaseClient
from plawright_clients.auth_client import AuthClient


class OrdersClient(BaseClient):

    def place_order(self, email, password):
        PAYLOAD = {
            "orders": [
                {
                    "country": "Antarctica",
                    "productOrderedId": "6960ea76c941646b7a8b3dd5"
                }
            ]
        }
        token = AuthClient(self.playwright).auth(email, password)
        place_order = self._post(url="api/ecom/order/create-order",
                                 data=PAYLOAD,
                                 headers={"Authorization": token})
        if not place_order.ok:
            raise ValueError(f"Login failed with status code {place_order.status_code}")
        order_id = place_order.json()["orders"][0]
        print(f"Created Order ID: {order_id}")
        return order_id
