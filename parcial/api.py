from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth

app = Flask(__name__)
basic_auth = BasicAuth(app)

# Clase de ejemplo
class Usuario:
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

# Lista de usuarios (simulación de una base de datos)
usuarios = []

# Configuración de autenticación básica
app.config['BASIC_AUTH_USERNAME'] = 'user'  # Cambia esto por tu nombre de usuario
app.config['BASIC_AUTH_PASSWORD'] = 'password'  # Cambia esto por tu contraseña

# Ruta para crear un nuevo usuario usando POST
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.get_json()

    if 'id' not in data or 'nombre' not in data or 'email' not in data:
        return jsonify({'mensaje': 'Faltan datos obligatorios'}), 400

    nuevo_usuario = Usuario(data['id'], data['nombre'], data['email'])
    usuarios.append(nuevo_usuario)

    return jsonify({'mensaje': 'Usuario creado con éxito'}), 201

# Ruta para obtener la lista de usuarios usando GET
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    usuarios_data = []
    for usuario in usuarios:
        usuarios_data.append({
            'id': usuario.id,
            'nombre': usuario.nombre,
            'email': usuario.email
        })
    return jsonify(usuarios_data)
    
if __name__ == '__main__':
    app.run(debug=True)
