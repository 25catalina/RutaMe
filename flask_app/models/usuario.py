from flask_app.config.mysqlconnection import connectToMySQL


class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @classmethod
    def save(cls, data):
        query = "INSERT INTO usuarios (nombre, apellido, email, password, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s, NOW(), NOW());"
        return connectToMySQL('Rutame').query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        result = connectToMySQL('Rutame').query_db(query, data)
        if len(result) < 1:
            return None
        return cls(result[0])