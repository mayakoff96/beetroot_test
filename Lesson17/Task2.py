class Library:

    existing_books = None

    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author):
        book = Book(name, year, author)
        self.books.append(book)
        self.authors.append(author)
        return book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year: int):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library(name='{self.name}', books={self.books}, authors={self.authors})"

    def __str__(self):
        return f"Library: {self.name}"


class Book:
    existing_books = 0

    def __init__(self, name: str, year: int, author):
        self.name = name
        self.year = year
        self.author = author
        Book.existing_books += 1

    def __repr__(self):
        return f"Book name = {self.name}, year = {self.year}, {self.author}"

    def __str__(self):
        return f"Book: {self.name} ({self.year}) by {self.author}"


class Author:

    def __init__(self, name: str, country: str, birthday: int):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author: name = {self.name}, country = {self.country}, birthday = {self.birthday}, books = {self.books}"

    def __str__(self):
        return f"author: {self.name}"


library = Library('Home library')
author1 = Author('Alexandre Dumas', 'France', 1802)
author2 = Author('Artur Conan Doyle', 'UK', 1930)

book1 = library.new_book('The Three Musketeers', 1844, author1)
book2 = library.new_book('A Study in Scarlet', 1887, author2)
book3 = library.new_book('The Sign of the Four', 1890, author2)

print(library)
print(book1)
print(book2)
print(book3)

print(Book.existing_books)

grouped_by_author = library.group_by_author(author1)
print(grouped_by_author)

grouped_by_year = library.group_by_year(1890)
print(grouped_by_year)
