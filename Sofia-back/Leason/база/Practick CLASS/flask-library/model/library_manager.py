import json
from book import Book
from user import User

class LibraryManager:
    _books_url = 'model/data/books.json'
    _user_url = 'model/data/users.json'

    def __init__(self):
        with open(self._books_url) as books_file:
            self.books = json.load(books_file)

        with open(self._user_url) as user_file:
            self.users = json.load(user_file)

        self.books = {book['book_id']: Book(**book) for book in self.books}
        self.users = {user['user_id']: User(**user) for user in self.users}

    def all_books(self):
        return self.books

    def find_book_by(self, **props):
        author = props.get('author')
        book_id = props.get('book_id')
        name = props.get('name')

        results = [book for book in self.books.values()]
        if author:
            results = [book for book in results if author.lower() in book.author.lower()]
        return results

    def return_books(self, user_id):
        user = self.users[user_id]
        user_books = user.borrowed_books[:]
        for book in user_books:
            user.return_book(self.books[book])
        else:
            return "All books returned"
    def get_user(self, user_id):
        info = self.users[user_id]
        user_book = user.borrowed_books[:]
        return info, user_book
    def add_user(self):
        id = len(self.users)
        name = input('Введите имя')
        new_user = {'id': id+1, 'name': name, "borrowed_books": []}
        self.users.append(self.users)
        return(self.users)

lm = LibraryManager()

user = lm.users[1]

user.borrow_book(lm.books[1]) # Borrow a book
user.borrow_book(lm.books[2]) # Borrow a book

print(user.borrowed_books) # [1, 2]
print(user.borrowed_books) # []
print(lm.add_user())
