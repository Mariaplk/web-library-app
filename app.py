from flask import Flask
from flask import render_template

from config import Config
from models import db


app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)


@app.route("/")
def index():

    return render_template(
        "index.html",
        books=[]
    )


@app.route("/login")
def login():

    return render_template(
        "login.html"
    )


@app.route("/books/<int:book_id>")
def book_view(book_id):

    return render_template(
        "book_view.html",
        book={},
        cover_url="",
        description_html=""
    )


@app.route("/books/create")
def create_book():

    return render_template(
        "book_form.html",
        title="Добавление книги",
        genres=[]
    )


@app.route("/books/<int:book_id>/edit")
def edit_book(book_id):

    return render_template(
        "book_form.html",
        title="Редактирование книги",
        genres=[]
    )


@app.route("/books/<int:book_id>/review")
def create_review(book_id):

    return render_template(
        "review_form.html"
    )


@app.route("/my-reviews")
def my_reviews():

    return render_template(
        "my_reviews.html",
        reviews=[]
    )


@app.route("/moderation")
def moderation():

    return render_template(
        "moderation.html",
        reviews=[]
    )


@app.route("/moderation/<int:review_id>")
def moderation_view(review_id):

    return render_template(
        "moderation_view.html",
        review={}
    )


if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(
        debug=True
    )
