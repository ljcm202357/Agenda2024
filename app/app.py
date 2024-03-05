from flask import Flask, render_template, redirect, request, url_for, flash, jsonify
import mysql.connector
# creamos una instancia de la clase flask

app = Flask(__name__)

# configurar la conexion
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Agenda2024"

)
cursor = db.cursor()


@app.route('/')
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
        db.commit()
        # flash('Usuario registrado correctamente', 'success')
        return redirect(url_for('lista'))
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
    app.secret_key = '28540464'
# definir rutas
