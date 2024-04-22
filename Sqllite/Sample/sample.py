# import sqlite3
#
# db = sqlite3.connect('books-collection.db')
# cursor = db.cursor()
# #
# # cursor.execute("CREATE TABLE books "
# #                "(id INTEGER PRIMARY KEY, "
# #                "title varchar(250) NOT NULL UNIQUE, "
# #                "author varchar(250) NOT NULL,"
# #                " rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

# ________________________________________________________________________________________________

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)


# Create a new declarative base class for the model
class Base(DeclarativeBase):
    pass


# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'

# create a new extension object
db = SQLAlchemy(model_class=Base)
# Initialize the database
db.init_app(app)


# create a table model
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


# create table schema
with app.app_context():
    db.create_all()

# CREATE ---> add a new book to the database
# with app.app_context():
#     new_book = Book(title='Mr Mickey Mouse', author=' Walt Disney', rating=7.3)
#     db.session.add(new_book)
#     db.session.commit()

# # READ ---> query all books
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.id))
    all_books = result.scalars()
    for book in all_books:
        print(f'{book.id}|{book.title}-{book.author}-{book.rating}')

# # Read A Particular Record By Query
# with app.app_context():
#     book = db.session.execute(db.select(Book).where(Book.id == 1)).scalar()
#     print(f'{book.title}|{book.author}|{book.rating}')


#
# #Update ---> A Particular Record By Query
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
#     book_to_update.title = "Harry Potter and the Chamber of Secrets"
#     db.session.commit()
#
# # Update--> A Record By PRIMARY KEY
# book_id = 1
# with app.app_context():
#     book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
#     # or book_to_update = db.get_or_404(Book, book_id)
#     book_to_update.title = "Harry Potter and the Goblet of Fire"
#     db.session.commit()

# DELETE ---> A Particular Record By Query
# with app.app_context():
#     book_to_delete = db.session.execute(db.select(Book).where(Book.id == 2)).scalar()
#     # or book_to_delete = db.get_or_404(Book, book_id)
#     db.session.delete(book_to_delete)
#     db.session.commit()