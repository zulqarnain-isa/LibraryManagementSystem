class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = available

    def borrow_book(self):
        if self.available:
            self.available = False
            return f"{self.title} has been borrowed."
        else:
            return f"{self.title} is currently not available."

    def return_book(self):
        self.available = True
        return f"{self.title} has been returned."

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.books_borrowed = []

    def borrow_book(self, book):
        if book.available:
            book.borrow_book()
            self.books_borrowed.append(book)
            print(f"{book.title} has been borrowed by {self.name}.")
        else:
            print(f"{book.title} cannot be borrowed because it is not available.")

    def return_book(self, book):
        if book in self.books_borrowed:
            book.return_book()
            self.books_borrowed.remove(book)
            print(f"{book.title} has been returned by {self.name}.")
        else:
            print(f"{self.name} does not have {book.title}.")

class Library:
    def __init__(self):
        self.catalog = {}
        self.members = {}

    def add_book(self, book):
        self.catalog[book.isbn] = book
        print(f"Added {book.title} to the library.")

    def remove_book(self, isbn):
        if isbn in self.catalog:
            removed_book = self.catalog.pop(isbn)
            print(f"Removed {removed_book.title} from the library.")
        else:
            print(f"No book found with the ISBN {isbn}")

    def add_member(self, member):
        self.members[member.member_id] = member
        print(f"Added member {member.name} to the library.")

    def find_book(self, isbn):
        return self.catalog.get(isbn, None)

# Create the library
library = Library()

# Add books to the library
books = [Book("1984", "George Orwell", "1234567890"),
    Book("Brave New World", "Aldous Huxley", "2345678901"),
    Book("To Kill a Mockingbird", "Harper Lee", "3456789012")]

for book in books:
    library.add_book(book)

# Add members to the library
members = [Member("Alice Johnson", "001"),
    Member("Bob Smith", "002"),
    Member("Charlie Brown", "003")]

for member in members:
    library.add_member(member)

# Borrowing books
members[0].borrow_book(books[0])  # Alice borrows "1984"
members[1].borrow_book(books[1])  # Bob borrows "Brave New World"
members[2].borrow_book(books[2])  # Charlie borrows "To Kill a Mockingbird"

# Returning books
members[0].return_book(books[0])  # Alice returns "1984"
members[1].return_book(books[1])  # Bob returns "Brave New World"

# Check availability
print(books[0].available)  # Should print True
print(books[1].available)  # Should print True