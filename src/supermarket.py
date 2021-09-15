
class Checkout:
    class Discount:
        def __init__(self, no_items, price):
            self.no_items = no_items
            self.price = price

    def __init__(self):
        self.prices = {}
        # self.total = 0
        self.discounts = {}
        self.items = {}

    def add_item(self, item):
        if item not in self.prices:
            raise Exception('Bad Item')
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def add_item_price(self, item, price):
        self.prices[item] = price

    def calculate_total(self):
        total = 0
        for item, cnt in self.items.items():
            total += self.calculate_item_total(item, cnt)
        return total

    def calculate_item_total(self, item, cnt):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if cnt >= discount.no_items:
                total += self.calculate_item_discount_total(item, cnt, discount)
            else:
                total += self.prices[item] * cnt
        else:
            total += self.prices[item] * cnt
        return total

    def add_discount(self, item, no_of_items, price):
        discount = self.Discount(no_of_items, price)
        self.discounts[item] = discount

    def calculate_item_discount_total(self, item, cnt, discount):
        total = 0
        no_of_discounts = cnt / discount.no_items
        total += no_of_discounts * discount.price
        remaining = cnt % discount.no_items
        total += remaining * self.prices[item]
        return total
