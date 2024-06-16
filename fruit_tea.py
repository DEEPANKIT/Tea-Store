from bubble_tea import BubbleTea

class FruitTea(BubbleTea):
    # Constants for prices
    TEA_TYPE_PRICES = {"Fruity": 0.15, "Milky": 0.29, "Sparkling": 0.19, "Hot": 0.24, "Frozen": 3}
    SIZE_PRICES = {"Small": 0, "Medium": 0.85, "Large": 1.2}
    FRUIT_PRICES = {
        "Mango": 0.3, "Lychee": 0.1, "Apple": 0.2, "Grape": 0.4, "Melon": 0.5,
        "Grapefruit": 0.1, "Lemon": 0.3, "Guava": 0.2, "Passionfruit": 0.25,
        "Strawberry": 0.2, "Pomegranate": 0.45, "Peach": 0.1, "Tropical": 0.65, "Watermelon": 0.35
    }
    FLAVOUR_PRICES = {
        "Mint Choc": 0.3, "Thai": 0.35, "Salted Caramel": 0.2, "Roasted": 0.4,
        "Earl Grey": 0.5, "Vanilla": 0.1, "Assam": 0.3, "Hazelnut": 0.2,
        "Oolong": 0.25, "Jasmine": 0.2
    }

    def __init__(self, name, size, ice_level, sugar_level, tea_type, fruit_flavour, flavour=None):
        super().__init__(name, size, ice_level, sugar_level, tea_type)
        self.fruit_flavour = fruit_flavour
        self.flavour = flavour

    def calculate_price(self):
        base_price = 4.5  # Base price for all teas
        price = base_price

        # Add tea type price
        price += self.TEA_TYPE_PRICES[self.tea_type]

        # Add size price
        price += self.SIZE_PRICES[self.size]

        # Add fruit price
        price += self.FRUIT_PRICES.get(self.fruit_flavour, 0)

        # Add flavour price (if applicable)
        if self.flavour:
            price += self.FLAVOUR_PRICES.get(self.flavour, 0)

        # Add topping prices
        for topping in self.toppings:
            price += topping.price

        return round(price, 2)

    def __str__(self):
        topping_names = ", ".join([t.name for t in self.toppings])
        return f"{self.name} ({self.size}) - Ice: {self.ice_level}, Sugar: {self.sugar_level}, Tea: {self.tea_type}, Toppings: {topping_names}, Fruit Flavour: {self.fruit_flavour}"
