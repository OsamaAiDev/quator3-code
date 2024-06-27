class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def eating(self, food: str)-> None:
        print(f"{self.name} is eating food {food}")


class Bird(Animal):
    def eating(self, food: str)-> None:
        print(f"Bird is eating food {food}")

my_animal: Animal = Bird("parrot")

my_animal.eating("fish")
print(my_animal.name)
print(type(my_animal))

# my_bird: Bird = Bird("sparrow")