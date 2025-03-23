# 1/2 Obligatorio Generico:
from flask import Flask, jsonify, request
app = Flask(__name__)
# Fin 1/2 Obligatorio Generico:

# A. Endpoint: /todos
todos = [
    {"label": "My first task", "done": False},
    {"label": "My second task", "done": False}
]

@app.route('/todos', methods=['GET'])
def hello():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.insert(0,request_body)
    json_text = jsonify(todos)
    return json_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    try:
        todos.pop(position)  # Elimina la tarea en la posición indicada
        return jsonify(todos), 200  # Retorna la lista actualizada con código 200
    except IndexError:
        return jsonify({"error": "Posición inválida"}), 400  # Manejo de error si la posición no es válida


# B. Endpoint: /myrote
some_data = {"name": "Bobby", "lastname": "Rixer"}

@app.route('/myroute', methods=['GET'])
def hello_world():
    json_text = jsonify(some_data)
    return json_text


# 2/2 Obligatorio Generico, siempre al final del archivo Py
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
# Fin 2/2 Obligatorio Generico, siempre al final del archivo Py
