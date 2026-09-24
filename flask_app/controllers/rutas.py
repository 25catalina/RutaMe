from flask_app import app #Importamos la app

from flask import render_template,redirect,request,session,flash


#importamos la clase que estamos controlando

from flask_app.models.ruta import Usuario


@app.route("/", methods=["GET", "POST"])
def registro():
    usuarios = Usuario.get_all()
    print(usuarios)
    return render_template("registro_inicio_sesion.html")

@app.route('/guardar',methods=['POST'])
def crear():
    datos = {
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "password": request.form['password']
    }
    Usuario.save(datos)
    return redirect('/usuarios')

@app.route('/usuarios')
def usuarios():
    usuarios = Usuario.get_all()
    return render_template("resultados.html",todos_usuarios = usuarios)

@app.route('/mostrar/<int:usuario_id>')
def detalle(usuario_id):
    datos = {
        'id': usuario_id
    }
    usuario = Usuario.get_one(datos)
    return render_template("detalle.html",usuario = usuario)

@app.route('/editar/<int:usuario_id>')
def editar(usuario_id):
    datos = {
        'id': usuario_id
    }
    usuario = Usuario.get_one(datos)
    return render_template("editar.html", usuario = usuario)

@app.route('/actualizar/<int:usuario_id>', methods=['POST'])
def actualizar(usuario_id):
    datos = {
        'id': usuario_id,
        "nombre": request.form['nombre'],
        "apellido": request.form['apellido'],
        "email": request.form['email'],
        "password": request.form['password']
    }
    Usuario.update(datos)
    return redirect(f"/mostrar/{usuario_id}")

@app.route('/borrar/<int:usuario_id>')
def borrar(usuario_id):
    datos = {
        'id': usuario_id,
    }
    Usuario.delete(datos)
    return redirect('/usuarios')