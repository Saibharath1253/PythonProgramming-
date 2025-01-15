class Publisher:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Publisher: {self.name}")

class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

class Python(Book):
    def __init__(self, name, title, author, price, pages):
        super().__init__(name, title, author)
        self.price = price
        self.pages = pages

    def display_info(self):
        super().display_info()
        print(f"Price: {self.price}")
        print(f"Pages: {self.pages}")


publisher_name = input("Enter publisher name: ")
book_title = input("Enter book title: ")
book_author = input("Enter book author: ")
price = float(input("Enter book price: "))
pages = int(input("Enter number of pages: "))

python_book = Python(publisher_name, book_title, book_author, price, pages)
python_book.display_info()
