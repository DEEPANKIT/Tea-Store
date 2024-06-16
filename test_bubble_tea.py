from fruit_tea import FruitTea
from topping import Topping

def test_add_topping():
    tea = FruitTea("Test Tea", "Small", "Normal", "Normal", "Fruity", "Mango")
    topping = Topping("Pearls", 1.2)
    tea.add_topping(topping)
    assert topping in tea.toppings

def test_remove_topping():
    tea = FruitTea("Test Tea", "Small", "Normal", "Normal", "Fruity", "Mango")
    topping = Topping("Pearls", 1.2)
    tea.add_topping(topping)
    tea.remove_topping(topping)
    assert topping not in tea.toppings

def test_calculate_price():
    tea = FruitTea("Test Tea", "Small", "Normal", "Normal", "Fruity", "Mango")
    assert tea.calculate_price() == 4.95  # Base price + 0.15 for fruity tea + 0.3 for mango
    topping = Topping("Pearls", 1.2)
    tea.add_topping(topping)
    assert tea.calculate_price() == 6.15  # Base price + 0.15 for fruity tea + 0.3 for mango + 1.2 for topping

def test_str_method():
    tea = FruitTea("Test Tea", "Small", "Normal", "Normal", "Fruity", "Mango")
    assert str(tea) == "Test Tea (Small) - Ice: Normal, Sugar: Normal, Tea: Fruity, Toppings: , Fruit Flavour: Mango"
    topping = Topping("Pearls", 1.2)
    tea.add_topping(topping)
    assert str(tea) == "Test Tea (Small) - Ice: Normal, Sugar: Normal, Tea: Fruity, Toppings: Pearls, Fruit Flavour: Mango"

if __name__ == "__main__":
    test_add_topping()
    test_remove_topping()
    test_calculate_price()
    test_str_method()
    print("All tests passed!")
