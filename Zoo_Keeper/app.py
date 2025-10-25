import sqlite3
class Animal():
    def __init__(self,name,species,sound):
        self.name = name
        self.species = species
        self.sound = sound
    def display_info(self):
        print(f"Name : {self.name} \n Species : {self.species} \n Sound : {self.sound}")
    def make_sound(self):
        print(F"I am a {self.name}...{self.sound}!!")
    def __str__(self):
        return(f"Name : {self.name} \n Species : {self.species} \n Sound : {self.sound}")
class Elephant(Animal):
    def __init__(self,name,species,sound):
        super().__init__(name,species,sound)
    def display_info(self):
        return super().display_info()
    def make_sound(self):
         print(F"I am a big {self.name}...{self.sound}!!")
class Lion(Animal):
    def __init__(self,name,species,sound):
        super().__init__(name,species,sound)
    def display_info(self):
        super().display_info()
    def make_sound(self):
        print(f"I am the king of the jungle... {self.sound}!!!")
class Monkey(Animal):
    def __init__(self, name, species, sound):
        super().__init__(name, species, sound)
    def display_info(self):
        return super().display_info()
    def make_sound(self):
        print(f"I am a {self.name} and i love bananas...")
    
animals = []
    

def save_elephant():
    name = "Elephant"
    species = "Hervial"
    sound = "Trumpet"
    elephant = Elephant(name,species, sound)
    elephant.display_info()
    elephant.make_sound()
    animals.append(elephant)

def save_lion():
    name ="Lion"
    species = "Carnival"
    sound = "ROOARR"
    lion = Lion(name,species, sound)
    lion.display_info()
    lion.make_sound()
    animals.append(lion)


def save_monkey():
    name ="Monkey"
    species = "Mammal"
    sound = "Krrrr"
    monkey = Monkey(name,species, sound)
    monkey.display_info()
    monkey.make_sound()
    animals.append(monkey)

save_elephant()
save_lion()
save_monkey()
for animal in animals:
    print(animal)

