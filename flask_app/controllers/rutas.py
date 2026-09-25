from flask_app import app
from flask import render_template, session

@app.route("/rutas")
def panel():
    return f"inicio  sesion/ registro completo: {session['user_id']}"