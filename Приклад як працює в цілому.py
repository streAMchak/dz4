if __name__ == "__main__":
    library = library() # type: ignore

    book1 = Book("Коти Вояки", "Фарбований Лис") # type: ignore
    book2 = Book("Кобзар", "Лісова пісня") # type: ignore

    library.add_book(book1)
    library.add_book(book2)

    library.borrow_book("Коти Вояки")
    library.borrow_book("Коти Вояки") 
    library.return_book("Коти Вояки")
    library.borrow_book("Коти Вояки")  
