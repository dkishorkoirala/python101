class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"Woof! I am {self.name} the {self.breed} dog.")

    def introduce(self):
        print(f"My name is {self.name} and I am a {self.breed}.")
d1 = Dog("coco", "shaperd")
d1.bark()
d1.introduce()


print("challenge")
class Cat:
    def __init__(self, name , color):
        self.name = name
        self.color= color
    
    def meow(self):
        print(f"Meow! I am {self.name} and a {self.color} cat.")
    
    def intro(self):
        print(f"My name is {self.name} and I am a {self.color} cat.")

c1 = Cat("mike", "black")
c1.meow()
c1.intro()

c2 = Cat("mona", "White")
c2.meow()
c2.intro()