from pet import Pet
from ninja import Ninja

pet_1 = Pet("Rolex", "Cat", ["sit", "roll over"])
ninja_1 = Ninja("Neri", "Alliu", pet_1, "sticks", "food")


ninja_1.feed()
ninja_1.walk()
ninja_1.bathe()