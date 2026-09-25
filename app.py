from flask_app import app
import flask_app.controllers.usuarios
import flask_app.controllers.rutas

if __name__ == "__main__":
    app.run(debug=True)