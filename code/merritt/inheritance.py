class Animal:
    def __init__(self, name, favorite_food):
        self.name = name
        self.favorite_food = favorite_food

    def print_me(self):
        print("this will never run unless you use super()")

class Mammal(Animal):
    def __init__(self, name, favorite_food):
        super().__init__(name, favorite_food)
        self.limbs = 4

    def print_me(self):
        print(f"Hi! I am a {self.type_of_animal} named {self.name}! I have {self.limbs} limbs and I love to eat {self.favorite_food}!")

class Squirrel(Mammal):
    def __init__(self, name, favorite_food):
        super().__init__(name, favorite_food)
        self.type_of_animal = 'fuzzy runners'

class Anteater(Mammal):
    def __init__(self, name, favorite_food):
        super().__init__(name, favorite_food)
        self.type_of_animal = 'bug slurpers'

class Snake(Animal):
    def __init__(self, name, favorite_food):
        super().__init__(name, favorite_food)
        self.limbs = 0
        self.type_of_animal = 'danger noodles'

    def print_me(self):
        print(f"DANGER TIME! I am a {self.type_of_animal} named {self.name}! I have {self.limbs} limbs and I love to eat {self.favorite_food}!")


s = Squirrel("Clarance", "peanuts")

a = Anteater("Jimmy", "ants")

n = Snake("Slithers the Snake", "eggs")

s.print_me()
a.print_me()
n.print_me()