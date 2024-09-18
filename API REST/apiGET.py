from flask import Flask

# Crear la aplicación Flask
app = Flask(__name__)

# Ruta para el método GET
@app.route('/saludo', methods=['GET'])
def saludo():
    return '¡Hola! Bienvenido a la API.'

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
