#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed
        
    def bark(self):
        print("Woof!")
    
    def get_adopted(self, owner_name):
        self.owner_name = owner_name   
    pass

my_dog = Dog(name="Dog")
print(f"My dog name is {my_dog.name} and the breed is {my_dog.breed}")
my_dog.bark()