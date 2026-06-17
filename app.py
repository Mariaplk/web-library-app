from flask import Flask, render_template

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


if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(
        debug=True
    )
