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
    def save(cls, datos):
        query = "INSERT INTO tacos (nombre, apellido, email, password) VALUES(%(nombre)s, %(apellido)s, %(email)s, %(password)s);"
        return connectToMySQL('Rutame').query_db(query, datos)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        usuarios_en_bd = connectToMySQL('Rutame').query_db(query)
        usuarios = []
        for usuario in usuarios_en_bd:
            usuarios.append(cls(usuario))
        return usuarios
    
    @classmethod
    def get_one(cls,datos):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        usuario_en_db = connectToMySQL('Rutame').query_db(query,datos)

        return cls(usuario_en_db[0])
    
    @classmethod
    def update(cls, datos):
        query = "UPDATE usuarios SET nombre=%(nombre)s, apellido=%(apellido)s, email=%(email)s, password=%(password)s WHERE id = %(id)s;"
        return connectToMySQL('Rutame').query_db(query, datos)
    
    @classmethod
    def delete(cls, datos):
        query = "DELETE FROM usuarios WHERE id = %(id)s;"
        return connectToMySQL('Rutame').query_db(query, datos)

class Ruta:
    def __init__(self, data):
            self.id = data['id']
            self.nombre = data['nombre']
            self.dificultad = data['dificultad']
            self.cupo= data['cupo']
            self.fecha = data['fecha']
            self.punto_de_encuentro = data['punto_de_encuentro']
            self.descripcion = data['descripcion']
            self.created_at = data['created_at']
            self.updated_at = data['updated_at']
            self.usuarios_id = data['usuarios_id']

class Inscripcion:
    def __init__(self, data):
            self.id = data['id']
            self.usuario_id = data['usuario_id']
            self.ruta_id = data['ruta_id']
            self.created_at = data['created_at']
            self.updated_at = data['updated_at']