class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.book_available = True


class User:
    def __init__(self, name):
        self.username = name
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def show_borrowed_books(self):
        print('\n=== Books borrowed by the user ===')
        for book in self.borrowed_books:
            print(book.title)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def lend_book(self, user, book):
        if book not in self.books:
            print('Book not in library')
            return

        if not book.book_available:
            print('Book not available')
            return

        user.borrow_book(book)
        book.book_available = False
        print(f'Book "{book.title}" issued to {user.username}')

    def show_books(self):
        print('\n=== Books in library ===')
        for book in self.books:
            status = 'Available' if book.book_available else 'Not available'
            print(f'{book.title}: {status}')


book1 = Book('Harry Potter and the Goblet of Fire', 'Joanne Rowling', 'Fantasy')
book2 = Book('1984', 'George Orwell', 'Dystopian literature')
book3 = Book('Fahrenheit 451', 'Ray Bradbury', 'Dystopian literature')

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.show_books()

user1 = User('Bohdan')

library.lend_book(user1, book1)

user1.show_borrowed_books()

library.show_books()
