from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY,  title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J.K.Rowling', '9.3')")
# db.commit()


app = Flask(__name__)
all_books = []

# CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    # Optional: this will allow each book object to be identified by its title when printed
    # def __repr__(self):
    #     return f'<Book {self.title}>'
    
# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# # CREATE Record
# with app.app_context():
#     new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating = 9.3)
#     db.session.add(new_book)
#     db.session.commit()

@app.route("/")
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars().all()
    return render_template("index.html" ,books=all_books)


@app.route("/add", methods = ["GET","POST"])
def add():
    if request.method == "POST":
        # new_book = {
        #     "title": request.form.get("title"),
        #     "author": request.form.get("author"),
        #     "rating": request.form.get("rating")
        # }
        # all_books.append(new_book)
        

        # CREATE RECORD
        new_book = Book(
            title = request.form["title"],
            author = request.form["author"],
            rating = request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))


    return render_template("add.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form["rating"] 
        db.session.commit()
        return redirect(url_for('home'))

    book_id = request.args.get('id')
    book_selected =db.get_or_404(Book, book_id) 
    return render_template("edit_rating.html", book= book_selected)

@app.route("/delete")
def delete():
    book_id = request.args.get("id")
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
