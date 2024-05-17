from flask import Flask, jsonify, request
from hdbcli import dbapi

app = Flask(__name__)

# Configuración de la conexión a SAP HANA
conn = dbapi.connect(
    address="52.152.107.200",
    port=30015,
    user="SYSTEM",
    password="Interpricek0",
    encrypt='true',
    sslValidateCertificate='false'
)

@app.route('/')
def holamundo():
    return 'Hola Mundo!'

# Rutas y funciones para QRIPL.USUARIOS
@app.route('/api/usuarios', methods=['GET'])
def get_usuarios():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM QRIPL.USUARIOS")
    rows = cursor.fetchall()
    cursor.close()

    usuarios = []
    for row in rows:
        usuario = {
            'ID': row[0],
            'USUARIO': row[1],
            'PWD': row[2],
            'SOCIO': row[3],
            'PERFIL': row[4],
            'ACTIVO': row[5]
        }
        usuarios.append(usuario)

    return jsonify(usuarios)

@app.route('/api/usuarios', methods=['POST'])
def crear_usuario():
    data = request.json
    cursor = conn.cursor()
    cursor.execute("INSERT INTO QRIPL.USUARIOS (USUARIO, PWD, SOCIO, PERFIL, ACTIVO) VALUES (%s, %s, %s, %s, %s)",
                   (data['USUARIO'], data['PWD'], data['SOCIO'], data['PERFIL'], data['ACTIVO']))
    conn.commit()
    cursor.close()

    return jsonify({'message': 'Usuario creado correctamente'})

@app.route('/api/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    data = request.json
    cursor = conn.cursor()
    cursor.execute("UPDATE QRIPL.USUARIOS SET USUARIO = %s, PWD = %s, SOCIO = %s, PERFIL = %s, ACTIVO = %s WHERE ID = %s",
                   (data['USUARIO'], data['PWD'], data['SOCIO'], data['PERFIL'], data['ACTIVO'], id))
    conn.commit()
    cursor.close()

    return jsonify({'message': 'Usuario actualizado correctamente'})

@app.route('/api/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM QRIPL.USUARIOS WHERE ID = %s", (id,))
    conn.commit()
    cursor.close()

    return jsonify({'message': 'Usuario eliminado correctamente'})

# Rutas y funciones para QRIPL.SOCIOS
@app.route('/api/socios', methods=['GET'])
def get_socios():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM QRIPL.SOCIOS")
    rows = cursor.fetchall()
    cursor.close()

    socios = []
    for row in rows:
        socio = {
            'ID': row[0],
            'SOCIO': row[1],
            'RFC': row[2],
            'ACTIVO': row[3]
        }
        socios.append(socio)

    return jsonify(socios)

@app.route('/api/socios', methods=['POST'])
def crear_socio():
    data = request.json
    cursor = conn.cursor()
    cursor.execute("INSERT INTO QRIPL.SOCIOS (SOCIO, RFC, ACTIVO) VALUES (%s, %s, %s)",
                   (data['SOCIO'], data['RFC'], data['ACTIVO']))
    conn.commit()
    cursor.close()

    return jsonify({'message': 'Socio creado correctamente'})

@app.route('/api/socios/<int:id>', methods=['PUT'])
def actualizar_socio(id):
    data = request.json
    cursor = conn.cursor()
    cursor.execute("UPDATE QRIPL.SOCIOS SET SOCIO = %s, RFC = %s, ACTIVO = %s WHERE ID = %s",
                   (data['SOCIO'], data['RFC'], data['ACTIVO'], id))
    conn.commit()
    cursor.close()

    return jsonify({'message': 'Socio actualizado correctamente'})

@app.route('/api/socios/<int:id>', methods=['DELETE'])
def eliminar_socio(id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM QRIPL.SOCIOS WHERE ID = %s", (id,))
    conn.commit()
    cursor.close()

    return jsonify({'message': 'Socio eliminado correctamente'})

# Rutas y funciones para QRIPL.PERFILES
@app.route('/api/perfiles', methods=['GET'])
def get_perfiles():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM QRIPL.PERFILES")
    rows = cursor.fetchall()
    cursor.close()

    perfiles = []
    for row in rows:
        perfil = {
            'ID': row[0],
            'PERFIL': row[1],
            'DESCRIPCION': row[2],
            'ACTIVO': row[3]
        }
        perfiles.append(perfil)

    return jsonify(perfiles)

@app.route('/api/perfiles', methods=['POST'])
def crear_perfil():
    data = request.json
    cursor = conn.cursor()
    cursor.execute("INSERT INTO QRIPL.PERFILES (PERFIL, DESCRIPCION, ACTIVO) VALUES (%s, %s, %s)",
                   (data['PERFIL'], data['DESCRIPCION'], data['ACTIVO']))
    conn.commit()
    cursor.close()

    return jsonify({'message': 'Perfil creado correctamente'})

@app.route('/api/perfiles/<int:id>', methods=['PUT'])
def actualizar_perfil(id):
    data = request.json
    cursor = conn.cursor()
    cursor.execute("UPDATE QRIPL.PERFILES SET PERFIL = %s, DESCRIPCION = %s, ACTIVO = %s WHERE ID = %s",
                   (data['PERFIL'], data['DESCRIPCION'], data['ACTIVO'], id))
    conn.commit()
    cursor.close()

    return jsonify({'message': 'Perfil actualizado correctamente'})

@app.route('/api/perfiles/<int:id>', methods=['DELETE'])
def eliminar_perfil(id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM QRIPL.PERFILES WHERE ID = %s", (id,))
    conn.commit()
    cursor.close()

    return jsonify({'message': 'Perfil eliminado correctamente'})

if __name__ == '__main__':
    app.run()