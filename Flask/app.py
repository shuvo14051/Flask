from flask import Flask, render_template, request, session
import datetime
from flask_session import Session 

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


notes = []


@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        note = request.form.get("note")
        note = note.capitalize()
        notes.append(note)
        return render_template('index.html', notes=notes)


if __name__ == '__main__':
    app.run()
