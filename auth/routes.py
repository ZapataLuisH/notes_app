from flask import Blueprint, flash, request, render_template, redirect, url_for

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        if username == "admin":
            return redirect(url_for("notes.home"))
        else:
            flash("Usuario no existe", "error")

    return render_template("login.html")
