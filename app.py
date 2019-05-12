from flask import Flask

#inicializacion de la aplicacion flask
app = Flask(__name__)

#se establece la ruta principal
@app.route('/')
def index():
    return 'Hola Mundo'

#configuracion basica
if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
