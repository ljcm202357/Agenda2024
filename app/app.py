<<<<<<< HEAD
from flask import Flask,render_template,request,redirect,url_for,jsonify,session
import mysql.connector
import bcrypt
#creamos una instancia de la clase flask
=======
from flask import Flask, render_template, redirect, request, url_for, flash, jsonify
import mysql.connector
# creamos una instancia de la clase flask
>>>>>>> 1e32c439200534e06cb5e18258119d7d8be5bc8a

app = Flask(__name__)

# configurar la conexion
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Agenda2024"

)
cursor = db.cursor()


<<<<<<< HEAD
def encriptarcontra(contraencrip):
    # generar un hash de la contraseña 
    encriptar = bcrypt.hashpw(contraencrip.encode('utf-8'),bcrypt.gensalt())

    return encriptar

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        #VERIFICAR LAS CREDENCIALES DEL USUARIO
        username = request.form.get('txtusuario')
        password = request.form.get('txtcontrasena')

        cursor = db.cursor()
        cursor.execute('SELECT usuarioper,contraper FROM personas where usuarioper = %s',(username,))
        usuarios = cursor.fetchone()

        if usuarios and bcrypt.check_password_hash(usuarios[7],password):
            session['usuario'] = username
            return redirect(url_for('lista'))
        else:
            error = 'Credenciales invalidas. por favor intentarlo de nuevo'
            return render_template('login.html',error=error)
        
    return render_template('login.html')    

=======
>>>>>>> 1e32c439200534e06cb5e18258119d7d8be5bc8a
@app.route('/')
def lista():

    # Recuperar datos de la tabla Personas
    cursor = db.cursor()
    cursor.execute("SELECT *  FROM personas")
    usuarios = cursor.fetchall()

    # Pasar los datos a un template HTML para mostrar la lista
    return render_template('index.html', personas=usuarios)

<<<<<<< HEAD

=======
>>>>>>> 1e32c439200534e06cb5e18258119d7d8be5bc8a

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

<<<<<<< HEAD
        Contrasenaencriptada = encriptarcontra(Contrasena)

        # Verificar si el usuario y el correo electrónico ya existen en la base de datos
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM Personas WHERE usuarioper = %s OR emailper = %s", (Usuario, Email))
        existing_user = cursor.fetchone()

        if existing_user:
            jsonify({'error': 'El usuario  o correo ya está registrado'})
            return redirect(url_for('registrar_usuario'))


    # insertar datos a la tabla personas

        cursor.execute("INSERT INTO Personas(nombreper,apellidoper,emailper,dirper,telper,usuarioper,contraper)VALUES(%s,%s,%s,%s,%s,%s,%s)",
                       (Nombres, Apellidos, Email, Direccion, Telefono, Usuario, Contrasenaencriptada))
=======
        # Verificar si el usuario y el correo electrónico ya existen en la base de datos
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM Personas WHERE usuarioper = %s OR emailper = %s", (Usuario, Email))
        existing_user = cursor.fetchone()

        if existing_user:
            jsonify({'error': 'El usuario  o correo ya está registrado'})
            return redirect(url_for('registrar_usuario'))

    # insertar datos a la tabla personas

        cursor.execute("INSERT INTO Personas(nombreper,apellidoper,emailper,dirper,telper,usuarioper,contraper)VALUES(%s,%s,%s,%s,%s,%s,%s)",
                       (Nombres, Apellidos, Email, Direccion, Telefono, Usuario, Contrasena))
>>>>>>> 1e32c439200534e06cb5e18258119d7d8be5bc8a
        db.commit()
        # flash('Usuario registrado correctamente', 'success')
        return redirect(url_for('lista'))
    # Redirigir a la misma página después de procesar la solicitud POST
        return redirect(url_for('registrar_usuario'))

    # Si la solicitud es GET, renderizar el formulario
    return render_template('Registrar.html')

<<<<<<< HEAD
@app.route('/editar/<int:id>',methods =['POST','GET'])
def editar_usuario(id):
    cursor = db.cursor()
    if request.method == 'POST':
        nombreper = request.form.get('nombreper')
        apellidoper = request.form.get('apellidoper')
        emailper = request.form.get('emailper')
        dirper = request.form.get('direccionper')
        telper = request.form.get('telefonoper')
        usuarioper = request.form.get('usuarioper')
        passper = request.form.get('passwordper')

        #sentencia para actualizar los datos
        sql = "UPDATE personas set nombreper=%s,apellidoper=%s,emailper=%s,dirper=%s,telper=%s,usuarioper=%s,contraper=%s where idper=%s"
        cursor.execute(sql,(nombreper,apellidoper,emailper,dirper,telper,usuarioper,passper,id))
        db.commit()

        return redirect(url_for('lista'))
    else:
        #obtener los datos de la persona que se va editar
        cursor = db.cursor()
        cursor.execute('SELECT * FROM personas WHERE idper  = %s',(id,))
        data = cursor.fetchall()

        return render_template('Editar.html', personas=data[0])

@app.route('/eliminar/<int:id>', methods=['GET'])
def eliminar_usuario(id):

=======

@app.route('/editar/<int:id>', methods=['POST', 'GET'])
def editar_usuario(id):
    # cursor = db.cursor()
    # cursor.execute('SELECT * FROM personas WHERE idper = %s', (id,))
    # data = cursor.fetchall()
    # cursor.close()
    # return render_template('editar.html', personas=data[0])
    cursor = db.cursor()

    if request.method == 'POST':
        nombre = request.form['nombreper']
        apellido = request.form['apellidoper']
        email = request.form['emailper']
        direccion = request.form['direccionper']
        telefono = request.form['telefonoper']
        usuario = request.form['usuarioper']
        contrasena = request.form['contrasenaper']

        # Actualizar los datos en la base de datos
        sql = "UPDATE personas SET nombreper=%s, apellidoper=%s, emailper=%s, dirper=%s, telper=%s, usuarioper=%s, contraper=%s WHERE idper=%s"
        cursor.execute(sql, (nombre, apellido, email, direccion,
                       telefono, usuario, contrasena, id))
        db.commit()

        # Redirigir a la página de lista después de editar
        return redirect(url_for('lista'))

    else:
        # Obtener los datos del usuario a editar
        cursor = db.cursor()
        cursor.execute('SELECT * FROM personas WHERE idper = %s', (id,))
        data = cursor.fetchall()
        cursor.close()
        return render_template('editar.html', personas=data[0])


@app.route('/eliminar/<int:id>', methods=['GET'])
def eliminar_usuario(id):
>>>>>>> 1e32c439200534e06cb5e18258119d7d8be5bc8a
    cursor = db.cursor()
    cursor.execute('DELETE FROM personas WHERE idper = %s', (id,))
    db.commit()
    cursor.close()
    return redirect(url_for('lista'))

<<<<<<< HEAD
#para ejecutar la aplicacion
if __name__ == '__main__':
    app.add_url_rule('/',view_func=lista)
    app.run(debug=True,port=5005)
#definir rutas
=======

# para ejecutar la aplicacion
if __name__ == '__main__':
    app.add_url_rule('/', view_func=lista)
    app.run(debug=True, port=5005)
    app.secret_key = '28540464'
# definir rutas
>>>>>>> 1e32c439200534e06cb5e18258119d7d8be5bc8a
