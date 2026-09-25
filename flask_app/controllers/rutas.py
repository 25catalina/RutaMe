from flask_app import app
from flask import render_template, session

@app.route("/rutas")
def panel():
    return f"Panel - user_id en sesion: {session['user_id']}"