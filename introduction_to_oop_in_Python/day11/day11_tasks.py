print("..............................................................................................................")

class Car:
    def __init__(self, brand, year, price):
        self.brand = brand
        self.year = year
        self.price = price

    def display_info(self):
        print(f"The car is of Brand: {self.brand}, of Year: {self.year}, and costs ${self.price}")

car1 = Car("Toyota", 1999, 200000)
car1.display_info()

car2 = Car("Hundai", 2000, 123456)
car2.display_info()

print("..............................................................................................................")

class Movie:
    def __init__(self, title, director, movyear):
        self.title = title
        self.director = director
        self.movyear = movyear
    
    def display_info(self):
        print(f"The movie is called {self.title}, directed by {self.director}, and was released in {self.movyear}")
    
    def is_classic(self):
        if self.movyear < 2000:
            print("Classic Movie")
        else:
            print("Modern movie")

movie1 = Movie("Titanic", "James Cameron", 1997)
movie1.display_info()
movie1.is_classic()

movie2 = Movie("Avengers", "Joss Whedon", 2012)
movie2.display_info()
movie2.is_classic()

print("..............................................................................................................")
