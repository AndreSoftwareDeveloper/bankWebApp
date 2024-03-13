from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SECRET_KEY"] = "DEBUG"
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
