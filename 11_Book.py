class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()

    @classmethod 
    def increment_book_count(cls):
        cls.total_books += 1

    @classmethod
    def get_total_books(cls):
        return cls.total_books
    
book1 = Book("Pyton Programming", "Eric Matthes")
book2 = Book("English", "William shakesphere")

print("Total Books:", Book.get_total_books())
print(f"{book1.title}, {book1.author}")

