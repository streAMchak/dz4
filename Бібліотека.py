class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Книга "{book.title}" добавлена в бібліотеку.')

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.borrow()
                return
        print(f'Книга "{title}" не знайдена в бібліотеці.')

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.return_book()
                return
        print(f'Книга "{title}" не знайдено в бібліотеці.')
