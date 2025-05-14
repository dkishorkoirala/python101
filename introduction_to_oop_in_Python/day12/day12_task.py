print("..................................task..................................\n")

class Laptop():
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def show_info(self):
        print(f"The laptop : {self.brand} model number {self.model}, price is ${self.price} ")

laptop1 = Laptop("Dell", 12323, 2000)
laptop1.show_info()
laptop2 = Laptop("Acer", 12345, 1500)
laptop2.show_info()
print("\n..................................task..................................")

print("\n..................................Challenge..................................")
class Pet():
    def __init__(self, name, animal_type, age):
        self.name = name
        self.animal_type = animal_type
        self.age = age
    
    def speak(self):
        if self.animal_type == "dog":
            print( "Woof!")
        elif self.animal_type == "cat":
            print( "Meow!")
        else :
            print( "Hello!")
        
dog = Pet("tommy", "dog", 2)
dog.speak()
cat = Pet("meow", "cat", 3)
cat.speak()
parrot = Pet("polly", "parrot", 4)
parrot.speak()
print("..................................Challenge..................................")