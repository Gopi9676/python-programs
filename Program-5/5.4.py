class Book:
    def __init__(self,title):
        self.title=title
    def create_book_list():
        return[Book("python 101"),Book("AI Basics"),Book("Data Science")]
books=Book.create_book_list()
for b in books:
    print("Book title:",b.title)
