print("............................................... COMPOSITION ...............................................")

class CPU:
    def __init__(self, cores):
        self.cores = cores

    def process(self):
        print(f"CPU with {self.cores} cores is processing data...")

class Computer:
    def __init__(self, brand, cores):
        self.brand = brand
        self.cpu = CPU(cores)  # Composition: CPU is created inside Computer

    def start_computer(self):
        print(f"{self.brand} computer is starting...")
        self.cpu.process()

# Test Composition
c = Computer("Dell", 8)
c.start_computer()

print("............................................... AGGREGATION ...............................................")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show_book(self):
        print(f"Book: {self.title} by {self.author}")

class Library:
    def __init__(self, library_name, book_list):
        self.library_name = library_name
        self.books = book_list  # Aggregation: books passed from outside

    def show_library(self):
        print(f"\nLibrary Name: {self.library_name}")
        print("Available Books:")
        for book in self.books:
            book.show_book()

# Create Books
book1 = Book("Python Basics", "Alice")
book2 = Book("AI for Beginners", "Bob")
book3 = Book("Deep Learning", "Carol")

# Create Library using existing Book objects
library = Library("City Library", [book1, book2, book3])
library.show_library()