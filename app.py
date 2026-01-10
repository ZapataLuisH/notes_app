from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

DB_FILE_PATH = os.path.join(
    os.path.dirname(__file__),
    'notes.sqlite'
)

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_FILE_PATH}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    create_note = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Note {self.id}: {self.title}>'


@app.route("/")
def home():
    role = "otro"
    notes = ["Nota 1", "Nota 2", "Nota 3"]
    return render_template('home.html', role=role, notes=notes)


@app.route("/acerca_de")
def about():
    return "Esto es una App de notas"


@app.route("/contacto", methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        return "Formulario enviado correctamente", 201
    return "Pagina de contacto"


@app.route("/api/info")
def api_info():
    data = {
        "nombre": "Notes App",
        "version": "1.1.1"
    }
    return jsonify(data), 200


@app.route("/confirmation")
def confirmation():
    return "Su mensaje ha sido recibido correctamente."


@app.route("/crear_nota", methods=['GET', 'POST'])
def create_note():
    if request.method == "POST":
        note = request.form.get('note', "No encontrada")
        return redirect(url_for('confirmation'))

    return render_template('note_form.html')
