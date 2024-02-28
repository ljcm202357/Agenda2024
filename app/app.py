from flask import Flask,render_template
import mysql.connector
#creamos una instancia de la clase flask

app = Flask(__name__)

#configurar la conexion
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Agenda2024"

)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Registrar', methods=['POST'])
def registrar_usuario():
    Nombres = request.form['nombre'],
    Apellidos = request.form['apellido'],
    Email = request.form['email'],
    Direccion = request.form['direccion'],
    Telefono = request.form['telefono'],
    Usuario = request.form['usuario'],
    Contrasena = request.form['contrasena']

    #insertar datos a la tabla personas

    cursor.execute("INSERT INTO Personas(nombreper,apellidoper,emailper,dirper,telper,usuarioper,contraper)VALUES(%s,%s,%s,%s,%s,%s,%s)",(Nombres,Apellidos,Email,Direccion,Telefono,Usuario,Contrasena))
    db.commit()

    return redirect(url_for('Registrar'))

#para ejecutar la aplicacion
if __name__ == '__main__':
    app.add_url_rule('/',view_func=index)
    app.run(debug=True,port=5005)
#definir rutas