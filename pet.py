class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 0
        self.energy = 0
    
    def sleep(self):
        self.energy += 25
        return self.energy

    def eat(self):
        self.energy += 5
        self.health +=10
        return self.energy, self.health

    def play(self):
        self.health += 5
        return self.health

    def noise(self):
        print("Brrrrrr")



