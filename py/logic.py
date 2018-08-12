import os
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///Users/Bis/Documents/Flask/py/users.db'
app.config['SQLALCHEMY_BINDS'] = {'riddle' : 'sqlite://///Users/Bis/Documents/Flask/py/riddle.db',
                                  'answer' : 'sqlite://///Users/Bis/Documents/Flask/py/answer.db'}

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True)
    message = db.Column(db.String(120), index=True, unique=True)

class Riddle(db.Model):
    __bind_key__ = 'riddle'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    riddle = db.Column(db.String(300), index=True, unique=True)

class Answer(db.Model):
    __bind_key__ = 'answer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    answer = db.Column(db.String(64), index=True, unique=True)


def write_to_file(filename, data):
    with open(filename, "a") as file:
        file.writelines(data)

@app.route("/layout", methods=['POST'])
def pickUsername():
    if request.method == 'POST':
        newUsername = User(request.form['username'])
        db.session.add(newUsername)
        db.session.commit()
    return render_template('layout.html')

@app.route("/" , methods=["GET", "POST"])
def home():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
