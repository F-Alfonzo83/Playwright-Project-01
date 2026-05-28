from page_objects.order_history import OrderHistory


class DashboadPage:
    def __init__(self, page):
        self.page = page

    def go_to_orders(self):
        ## GO TO ORDERS PAGE
        self.page.get_by_role("button", name="ORDERS").click()
        return OrderHistory(self.page)

    def get_products(self):
        cards_locator = self.page.locator("section#products>div.container div.row div.card")
        return cards_locator.all()

    def get_product_cards_names(self):
        cards = self.get_products()
        card_names = [card.locator("h5").inner_text() for card in cards]
        return card_names

