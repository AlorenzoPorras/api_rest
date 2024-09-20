from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# URL de la base de datos
BASE_URL = 'https://66eb01a455ad32cda47b4d0a.mockapi.io/IoTCarStatus'


# Obtener todos los registros (READ - GET)
@app.route('/status', methods=['GET'])
def get_status():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({'error': 'Error al obtener los datos'}), response.status_code


# Obtener un registro específico por ID (READ - GET)
@app.route('/status/<id>', methods=['GET'])
def get_status_by_id(id):
    response = requests.get(f'{BASE_URL}/{id}')
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({'error': f'Error al obtener el registro con ID {id}'}), response.status_code


# Crear un nuevo registro (CREATE - POST)
@app.route('/status', methods=['POST'])
def create_status():
    new_data = request.json  # Los datos enviados en el body de la solicitud
    response = requests.post(BASE_URL, json=new_data)
    if response.status_code == 201:
        return jsonify(response.json()), 201
    else:
        return jsonify({'error': 'Error al crear el registro'}), response.status_code


# Actualizar un registro existente por ID (UPDATE - PUT)
@app.route('/status/<id>', methods=['PUT'])
def update_status(id):
    updated_data = request.json  # Los datos enviados en el body de la solicitud
    response = requests.put(f'{BASE_URL}/{id}', json=updated_data)
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({'error': f'Error al actualizar el registro con ID {id}'}), response.status_code


# Eliminar un registro por ID (DELETE - DELETE)
@app.route('/status/<id>', methods=['DELETE'])
def delete_status(id):
    response = requests.delete(f'{BASE_URL}/{id}')
    if response.status_code == 200:
        return jsonify({'message': f'Registro con ID {id} eliminado correctamente'}), 200
    else:
        return jsonify({'error': f'Error al eliminar el registro con ID {id}'}), response.status_code


# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
