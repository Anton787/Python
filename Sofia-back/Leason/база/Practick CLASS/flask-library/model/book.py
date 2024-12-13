class Book:
    def __init__(self, book_id, title, author, borrowed_by_user_id=None):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.borrowed_by_user_id = borrowed_by_user_id

    def get_info(self, user=True):
        info = {'book_id': self.book_id, 'title': self.title, 'author': self.author}
        if user:
            info['borrowed_by_user_id'] = self.borrowed_by_user_id
        return info

    def is_available(self):
        return self.borrowed_by_user_id is None

    def set_borrow(self, user_id):
        self.borrowed_by_user_id = user_id if self.is_available() else None