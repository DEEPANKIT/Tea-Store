from fruit_tea import FruitTea
from topping import Topping

class Store:
    def __init__(self):
        self.earnings = 0
        self.order_history = []

    def order_tea(self, tea):
        self.earnings += tea.calculate_price()
        self.order_history.append(tea)

    def display_order_history(self):
        for order in self.order_history:
            print(order)
