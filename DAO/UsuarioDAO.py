from DAO.Conexion import Conexion
from DTO.Usuario import Usuario
import pymysql
import bcrypt

host='localhost'
user="root"
password=''
db='empresa'

@staticmethod
def login(username, password):
    con = None
    try:
        # Abrir la conexión a la base de datos
        con = Conexion(host, user, password, db)
        cursor = con.cursor()

        # Consulta SQL para obtener los datos del usuario
        sql = "SELECT * FROM usuarios WHERE usuario = %s"
        cursor.execute(sql, (username,))
        datos = cursor.fetchone()

        if datos:
            # Obtener la contraseña almacenada y compararla con la contraseña proporcionada
            hashed_password = datos[2].encode('utf-8')
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                return datos
            else:
                return None
        else:
            return None
    except pymysql.Error as e:
        print("Error de base de datos:", e)
        return None
    except Exception as e:
        print("Error:", e)
        return None
    finally:
        # Cerrar la conexión a la base de datos
        if con:
            con.desconectar()
            
def add(username,password_hash,rol):
    try:
        con=Conexion(host,user,password,db)
        sql=f"insert into usuarios(usuario,contraseña,rol)"\
            f"values ('{username}','{password_hash}','{rol}') "
        con.ejecuta_query(sql)
        con.commit()
        return True
    except Exception as e:       
        print(f'Error al ejercutar la consulta. Error: {e}')
        con.rollback()
        return False
    
@staticmethod
def registrar_usuario(username, password_hash,rol):
    hashed_password=bcrypt.hashpw(password_hash.encode('utf-8'),bcrypt.gensalt())
    nuevo_usuario=Usuario(
        username=username,
        password_hash=hashed_password,
        rol=rol
    )
    con=Conexion(host,user,password,db)
    exito=add(
        username=nuevo_usuario.getUsername(),
        password_hash=nuevo_usuario.getPassword_Hash().decode('utf-8'),
        rol=nuevo_usuario.getRol()
        )
    if exito:
        print('Usuario Registrado Correctamente!!!')
        return nuevo_usuario
    else:
        print('Error al registrar el Usuario')
        return None
    