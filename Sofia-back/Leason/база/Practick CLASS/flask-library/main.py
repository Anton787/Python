from flask import Flask, jsonify, abort
from model.library_manager import LibraryManager
import json

app = Flask(__name__)
with open('model/data/books.json') as books_file: 
    books = json.load(books_file)
with open('model/data/users.json') as user_file: 
    users = json.load(user_file)
library = LibraryManager(books, users)

@app.route('/')
def hello():
    return 'Hello!'

@app.route('/book/<int:id>')
def get_book(id):
    book = library.books.get(id)
    if not book:
        abort(404)
    return jsonify(book.get_info())

# @app.route('/books')
# def get_books():
#     all_book = library.books
#     if not books:
#         abort(404)
#     return jsonify(all_book)

if __name__ == '__main__':
    app.run(debug=True)