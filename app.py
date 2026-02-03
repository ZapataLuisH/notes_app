from flask import Flask, request, jsonify, render_template, redirect, url_for
from config import Config
from models import Note, db
from notes.routes import notes_bp
from auth.routes import auth_bp


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(notes_bp)
app.register_blueprint(auth_bp)


@app.route("/acerca_de")
def about():
    return "Esto es una App de notas"


@app.route("/contacto", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        return "Formulario enviado correctamente", 201
    return "Pagina de contacto"
