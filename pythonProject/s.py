class Book:
    total_books=0
    def __init__(self,title,author):
        self.title=title
        self.author=author
        Book.total_books += 1
    @classmethod
    def _string(cls,book_str):
       title, author = book_str.split("-")
       return cls(title,author)

    @staticmethod
    def _valid_title(title):
        return len(title) >= 3




b1 = Book("Python Basics", "John")
b2 = Book._string("AI Guide-Smith")


print(Book.total_books)
print(Book._valid_title("Hi"))
print(Book._valid_title("Book"))










