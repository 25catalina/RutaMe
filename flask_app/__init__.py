from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "clave_secreta_rutame"
bcrypt = Bcrypt(app)


from flask_app.controllers import usuarios
from flask_app.controllers import rutas