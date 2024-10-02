class Book: 
    def __init__(self, title='FJFBIFBF', author='Gagelganc', year=2011, is_available=True):
        self.title = title
        self.author = author 
        self.year = year
        self.is_available = is_available

class Library:
    all_books = {}
    def add_book(self, book):
        self.all_books[book.title] = book
        print(f'Книга добавлена \n в библеотеке {self.all_books.keys()}')
    
    def remove_book(self, title):
        del self.all_books[title]
        print(f'Книга {title} пропала...')
        
    def end_book(self, title):
        if self.all_books[title].is_available:
            self.all_books[title].is_availbale = False
            print(f'Книга {self.all_books[title].title} выдана!')
        else:
            print('Книга отстутствует :(')
    
    def return_book(self, title):
        self.all_books[title].is_availbale = True
        print(f'Книга {self.all_books[title].title} вернулась!')
        
    def find_book_by_author(self, author):
        books = list(filter(lambda elem: elem.author == author, self.all_books.values()))
        for book in books:
            print(f'Есть следующие книги автора "{author}" {book.title} \n')


b1 = Book(title='Harry Potter', author='Anton', year=2024)
b4 = Book(title='Harry Potter 2', author='Anton', year=2025)
b2 = Book(title='Dota tutorial', author='Ne Anton', year=2010)
b3 = Book(title='KNIGA', author='Oleg', year=203)

l1 = Library()

l1.add_book(b1)
l1.add_book(b2)
l1.add_book(b3)
l1.add_book(b4)

l1.remove_book('KNIGA')
l1.end_book('Dota tutorial')
l1.return_book('Dota tutorial')
l1.find_book_by_author('Anton')