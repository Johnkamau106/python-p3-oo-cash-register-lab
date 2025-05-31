class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.transactions = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.transactions.append((title, price, quantity))

    def apply_discount(self):
        if self.discount:
            self.total -= self.total * (self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.transactions:
            last_item = self.transactions.pop()
            title, price, quantity = last_item
            self.total -= price * quantity
            for _ in range(quantity):
                self.items.remove(title)
