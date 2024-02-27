from flask import Flask,render_template

#creamos una instancia de la clase flask

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Registrar')
def saludos():
    return render_template('Registrar.html')

#para ejecutar la aplicacion
if __name__ == '__main__':
    app.add_url_rule('/',view_func=index)
    app.run(debug=True,port=5005)
#definir rutas