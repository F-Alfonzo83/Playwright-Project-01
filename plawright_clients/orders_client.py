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
        token = AuthClient(self.playwright).auth( email, password)
        place_order = self._post(url="api/ecom/order/create-order",
                                        data=PAYLOAD,
                                       headers={"Authorization": token})
        assert place_order.ok
        orderId = place_order.json()["orders"][0]
        print(f"Created Order ID: {orderId}")
        return orderId
