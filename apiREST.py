from flask import Flask

# Crear la aplicación Flask
app = Flask(__name__)

# Ruta para el método GET
@app.route('/saludo', methods=['GET'])
def saludo_get():
    return '¡Hola! Bienvenido a la API (GET).'

# Ruta para el método POST
@app.route('/saludo', methods=['POST'])
def saludo_post():
    return '¡Has enviado una solicitud POST!'

# Ruta para el método PUT
@app.route('/saludo', methods=['PUT'])
def saludo_put():
    return '¡Has enviado una solicitud PUT!'

# Ruta para el método DELETE
@app.route('/saludo', methods=['DELETE'])
def saludo_delete():
    return '¡Has enviado una solicitud DELETE!'

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
