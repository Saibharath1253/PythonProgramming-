class Publisher:
    def _init_(self, name):
        self.name = name

    def display_info(self):
        print(f"Publisher: {self.name}")

class Book(Publisher):
    def _init_(self, name, title, author):
        super()._init_(name)
        self.title = title
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

class Python(Book):
    def _init_(self, name, title, author, price, pages):
        super()._init_(name, title, author)
        self.price = price
        self.pages = pages
