from typing import List
import csv


class Item:
    pay_rate: float = 0.8 # pay rate after 80% discount
    all_items: List = []
    def __init__(self, name: str, price: float, quantity = 0) -> None:
        # Run validation to the recievied arguments
        assert price >=0, f"Price {price} is not greater than 0"
        assert quantity >=0, f"Quantity {quantity} is not greater than 0"

        # Assign attributes to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Add item to the items list
        Item.all_items.append(self)

    def calculate_total_cost(self) -> float:
        return self.price * self.quantity
    
    def apply_discount(self):
        # override the price attribute
        self.price = self.price * self.pay_rate
    # magic methods stands for representing new objects
    # returing string that is responsible for representing this object
    @classmethod    
    def instantiate_from_csv(cls):
        with open("./items.csv") as f:
            reader = csv.reader(f)
            items = list(reader)
            print(items)
    def __repr__(self) -> str:
        return f"Item('{self.name}', '{self.price}', '{self.quantity}')"
    

# item1: Item = Item("Phone", 300, 12)

# print(item1.calculate_total_cost())
# pehla pay rate ko instance level pr find kre ga nai mila ga tu class level pr find kre ga
# print(item1.pay_rate)


# dict is magic attribute take all the attributes and convert them into a dictionary

# print(Item.__dict__) # all the attributes at class level
# print(item1.__dict__) # all the attributes at instance level

# bad way we are manually adding attributes

# item1 = Item()
# item1.name = "phone"
# item1.price = 100

# here apply 30% discount to specific items not on all items
# item2: Item = Item("Laptop", 500, 30)
# item2.pay_rate = 0.7
# item2.apply_discount()
# print(item2.price)

# print(Item.all_items)

# for instance in Item.all_items:
#     print(instance.name)
    
Item.instantiate_from_csv()