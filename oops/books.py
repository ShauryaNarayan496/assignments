class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    def make_discount(self,discount):
        self.price = self.price * (1 - (discount/100))
        return self.price
class TextBook(Book):
    def __init__(self, title, author, price, subject):
        super().__init__(title, author, price)
        self.subject = subject

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)
book2 = TextBook("The Great Gatsby", "F. Scott Fitzgerald", 10.99, "English")
print(book1)
print(book1.make_discount(20))
print(book2)
print(book2.subject)
# in this exercise we have defined a class Book  with few properties and methods and a subclass TextBook with few properties and methods 