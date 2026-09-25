from flask_app import app, bcrypt
from flask import render_template, request, redirect, session, flash
from flask_app.models.usuario import Usuario

@app.route("/")
def index():
    return render_template("registro_inicio_sesion.html")

@app.route("/registrar", methods=["POST"])
def registrar():
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "password": pw_hash
    }
    usuario_id = Usuario.save(data)
    session['user_id'] = usuario_id
    return redirect("/rutas")

@app.route("/login", methods=["POST"])
def login():
    usuario = Usuario.get_by_email({"email": request.form['email']})
    if not usuario:
        flash("Credenciales inválidas", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(usuario.password, request.form['password']):
        flash("Credenciales inválidas", "login")
        return redirect("/")
    session['user_id'] = usuario.id
    return redirect("/rutas")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")