from flask import Flask, jsonify
from config import config
from flask_mysqldb import MySQL

app = Flask(__name__)

conexion = MySQL(app)

@app.route('/usuarios', methods = ['GET'])
def listar_usuarios():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT id, usuario, email, contraseña, rol FROM usuarios"
        cursor.execute(sql)
        datos = cursor.fetchall()
        usuarios = []
        for fila in datos:
            usuario = {'id': fila[0], 'usuario': fila[1], 'email': fila[2], 'contraseña': fila[3], 'rol': fila[4]} 
            usuarios.append(usuario)
        return jsonify({'usuarios': usuarios, 'mensaje': "Usuario registrado"})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})
    
@app.route('/usuarios/<id>', methods = ['GET'])    
def leer_usuario(id):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT id, usuario, email, contraseña, rol FROM usuario WHERE id = '{0}'".format(id)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            usuario = {'id': datos[0], 'usuario': datos[1], 'email': datos[2], 'contraseña': datos[3], 'rol': datos[4]} 
            return jsonify({'usuario': usuario, 'mensaje': "Usuario encontrado"})
        else:
            return jsonify({'mensaje': "Usuario NO encontrado"})
    except Exception as ex:
        return jsonify({'mensaje': "Error"})
    
def pagina_no_encontrada(error):
    return "<h1>La pagina que intentas buscar no existe... </h1>"

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()
