from book import Book

class User:
    def __init__(self, user_id, name, borrowed_books = []):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = [] + borrowed_books

    def borrow_book(self, book: Book):
        book_id = book.book_id
        if book.is_available():
            self.borrowed_books.append(book_id)
            book.set_borrow(self.user_id)
            return {"status": True, "message": "Book borrowed successfully"}
        return {"status": False, "message": "Book is not available"}
        

    def return_book(self, book: Book):
        if book.book_id in self.borrowed_books:
            self.borrowed_books.remove(book.book_id)
            book.set_borrow(None)
            print({"status": True, "message": "Book returned successfully"})
