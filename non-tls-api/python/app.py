from flask import Flask, request, jsonify

app = Flask(__name__)

# Datos de ejemplo (simulación de una base de datos)
data = []

# Ruta para obtener data los elementos
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)

# Ruta para agregar un elemento
@app.route('/data', methods=['POST'])
def add_todo():
    new_todo = request.json
    data.append(new_todo)
    return jsonify(new_todo), 201

# Ruta para eliminar un elemento por su índice
@app.route('/data/<int:index>', methods=['DELETE'])
def delete_todo(index):
    if 0 <= index < len(data):
        del data[index]
        return '', 204
    else:
        return jsonify({"message": "Índice no válido"}), 404

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
