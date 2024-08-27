class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.owner = owner
        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception("Not a valid pet type!")
        Pet.all.append(self)
        


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("Not pet type inserted!")

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda x: x.name)
    
    
# breakpoint()