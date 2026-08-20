import json


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} - {self.author} ({self.year})"


def book_to_dict(book):
    return {
        "title": book.title,
        "author": book.author,
        "year": book.year
    }


def dict_to_book(data):
    return Book(
        data["title"],
        data["author"],
        data["year"]
    )


def save_book(book):
    data = book_to_dict(book)

    with open("book.json", "w") as file:
        json.dump(data, file, indent=4)


def load_book():
    with open("book.json", "r") as file:
        data = json.load(file)

    return dict_to_book(data)


# =========================
# PROGRAMA
# =========================

book = Book(
    "1984",
    "George Orwell",
    1949
)

print("Objeto original:")
print(book)

save_book(book)

print("\nLivro salvo!")

del book

book = load_book()

print("\nObjeto carregado:")
print(book)