from abc import ABC, abstractmethod
from topping import Topping
class BubbleTea(ABC):

class BubbleTea(ABC):
    def __init__(self, name, size, ice_level, sugar_level, tea_type):
        self.name = name
        self.size = size
        self.ice_level = ice_level
        self.sugar_level = sugar_level
        self.tea_type = tea_type
        self.toppings = []
        self.base_price = 4.5

    @abstractmethod
    def calculate_price(self):
        pass

    def add_topping(self, topping):
        self.toppings.append(topping)

    def remove_topping(self, topping):
        self.toppings.remove(topping)

    def __str__(self):
        topping_names = ", ".join([t.name for t in self.toppings])
        return f"{self.name} ({self.size}) - Ice: {self.ice_level}, Sugar: {self.sugar_level}, Tea: {self.tea_type}, Toppings: {topping_names}"
