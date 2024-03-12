from flask import Flask, render_template, redirect, request, url_for, flash, jsonify, session
import mysql.connector
import bcrypt
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
import logging
# creamos una instancia de la clase flask

app = Flask(__name__)
# Este error indica que estás intentando usar sesiones en tu aplicación Flask,
# pero no has configurado una clave secreta (secret_key).
# La clave secreta es necesaria para firmar las sesiones y garantizar su seguridad.
app.secret_key = '51935349'

# configurar la conexion
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Agenda2024"

)
cursor = db.cursor()

# Configurar el registro
logging.basicConfig(level=logging.DEBUG)


def encriptarcontra(contraencrip):
    # generar un hash de la contraseña
    encriptar = bcrypt.hashpw(contraencrip.encode('utf-8'), bcrypt.gensalt())

    return encriptar


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        # VERIFICAR LAS CREDENCIALES DEL USUARIO
        username = request.form.get('txtusuario')
        password = request.form.get('txtcontrasena')

        cursor = db.cursor()
        cursor.execute(
            "SELECT usuarioper,contraper FROM personas where usuarioper = %s", (username,))
        usuarios = cursor.fetchone()

        if usuarios and check_password_hash(usuarios[1], password):
            session['usuario'] = username
            print(username)
            print(session['usuario'])
            return redirect(url_for('principal'))

        else:
            error = 'Credenciales invalidas. por favor intentarlo de nuevo'
            return render_template('login.html', error=error)

    return render_template('login.html')


@app.route('/logout')
def logout():
    # Elimina el nombre de usuario de la sesión
    session.pop('usuario', None)
    return redirect(url_for('login'))

# NO ALMACENAR CACHE DE LA PAGINA


@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


@app.route('/principal', methods=['GET', 'POST'])
def principal():
   # Verificar si el usuario ha iniciado sesión
    if 'usuario' in session:
        # Obtener el nombre de usuario de la sesión
        nombre_usuario = session['usuario']
        # Renderizar la plantilla de Principal.html
        return render_template('prin.html', nombre_usuario=nombre_usuario)
    else:
        # Si el usuario no ha iniciado sesión, redirigirlo a la página de inicio de sesión
        return redirect(url_for('login'))


@app.route('/lista', methods=['GET', 'POST'])
def lista():

    # Recuperar datos de la tabla Personas
    cursor = db.cursor()
    cursor.execute("SELECT *  FROM personas")
    usuarios = cursor.fetchall()

    # Pasar los datos a un template HTML para mostrar la lista
    return render_template('index.html', personas=usuarios)


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
        Contrasenaencriptada = generate_password_hash(Contrasena)

        # Verificar si el usuario y el correo electrónico ya existen en la base de datos
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM personas WHERE usuarioper = %s OR emailper = %s", (Usuario, Email))
        existing_user = cursor.fetchone()

        if existing_user:
            error = 'El usuario o correo ya está registrado.'
            return render_template('Registrar.html', error=error)

    # insertar datos a la tabla personas

        cursor.execute("INSERT INTO Personas(nombreper,apellidoper,emailper,dirper,telper,usuarioper,contraper)VALUES(%s,%s,%s,%s,%s,%s,%s)",
                       (Nombres, Apellidos, Email, Direccion, Telefono, Usuario, Contrasenaencriptada))
        db.commit()
        # flash('Usuario registrado correctamente', 'success')
        return redirect(url_for('login'))
    # Redirigir a la misma página después de procesar la solicitud POST
        return redirect(url_for('registrar_usuario'))

    # Si la solicitud es GET, renderizar el formulario
    return render_template('Registrar.html')


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
    cursor = db.cursor()
    cursor.execute('DELETE FROM personas WHERE idper = %s', (id,))
    db.commit()
    cursor.close()
    return redirect(url_for('lista'))


# para ejecutar la aplicacion
if __name__ == '__main__':
    app.add_url_rule('/', view_func=lista)
    app.run(debug=True, port=5005)

# definir rutas
