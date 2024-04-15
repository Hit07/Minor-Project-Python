from flask import Flask, render_template, request, redirect, url_forfrom flask_wtf import FlaskForm, CSRFProtectfrom wtforms import StringField, SubmitFieldfrom wtforms.validators import DataRequiredfrom flask_sqlalchemy import SQLAlchemyfrom sqlalchemy.orm import DeclarativeBase, Mapped, mapped_columnfrom sqlalchemy import Integer, String, Floatapp = Flask(__name__)class Base(DeclarativeBase):    passapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookstore-collection.db'db = SQLAlchemy(model_class=Base)db.init_app(app)all_books = []class Book_Store(db.Model):    id: Mapped[int] = mapped_column(Integer, primary_key=True)    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)    author: Mapped[str] = mapped_column(String(250), nullable=False)    rating: Mapped[str] = mapped_column(Float, nullable=False)    def __repr__(self):        return f'<Book {self.title}>'with app.app_context():    db.create_all()class BookForm(FlaskForm):    book = StringField('Book Name', validators=[DataRequired()])    submit = SubmitField('Submit')@app.route('/')def home():    with app.app_context():        result = db.session.execute(db.select(Book_Store).order_by(Book_Store.id))        all_books = result.scalars()        return render_template('index.html', books=all_books)@app.route("/add", methods=["GET", "POST"])def add():    if request.method == "POST":        with app.app_context():            new_book = Book_Store(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])            db.session.add(new_book)            db.session.commit()        return render_template('index.html', books=all_books)    return render_template("add.html")@app.route("/delete/<int:id>", methods=["POST"])def delete(id):    if request.method == "POST":        with app.app_context():            book_to_delete = Book_Store.query.get(id)            if book_to_delete:                db.session.delete(book_to_delete)                db.session.commit()                return "Book deleted successfully"            else:                return "Book not found"    else:        # Return a response for non-POST requests        return "Method Not Allowed", 405if __name__ == "__main__":    app.run(debug=True)