class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True 

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f'Ви взяли книгу: {self.title}')
        else:
            print(f'Книга "{self.title}" недоступна.')

    def return_book(self):
        self.is_available = True
        print(f'Ви вернули книгу: {self.title}')


