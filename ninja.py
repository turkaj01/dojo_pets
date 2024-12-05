from pet import Pet

class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    
    def walk(self):
        print(f"Ninja {self.first_name} {self.last_name} is walking the {self.pet.name}.")
        self.pet.play()

    def feed(self):
        print(f"Ninja {self.first_name} {self.last_name} is feeding the {self.pet.name}.")
        self.pet.eat()

    def bathe(self):
        print(f"Ninja {self.first_name} {self.last_name} is cleaning the {self.pet.name}.")
        self.pet.noise()