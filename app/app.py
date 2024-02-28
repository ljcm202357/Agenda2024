from flask import Flask,render_template,redirect,request,url_for
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

@app.route('/Registrar', methods=['GET', 'POST'])
def registrar_usuario():
    if request.method == 'POST':
       Nombres = request.form.get('nombre')
       Apellidos = request.form.get('apellido')
       Email = request.form.get('email')
       Direccion = request.form.get('direccion')
       Telefono = request.form.get('telefono')
       Usuario = request.form.get('usuario')
       Contrasena = request.form.get('contrasena')

    #insertar datos a la tabla personas

       cursor.execute("INSERT INTO Personas(nombreper,apellidoper,emailper,dirper,telper,usuarioper,contraper)VALUES(%s,%s,%s,%s,%s,%s,%s)",(Nombres,Apellidos,Email,Direccion,Telefono,Usuario,Contrasena))
       db.commit()

    # Redirigir a la misma página después de procesar la solicitud POST
       return redirect(url_for('registrar_usuario'))

    # Si la solicitud es GET, renderizar el formulario
    return render_template('Registrar.html')

#para ejecutar la aplicacion
if __name__ == '__main__':
    app.add_url_rule('/',view_func=index)
    app.run(debug=True,port=5005)
#definir rutas