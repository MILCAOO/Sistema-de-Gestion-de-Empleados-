from DAO.Conexion import Conexion
from DTO.Roles import Roles
import pymysql

host='localhost'
user="root"
password=''
db='empresa'

def add(rol):
    try:
        #Abre la conexion hacia la base de datos
        con=Conexion(host,user,password,db)
        sql=f"INSERT INTO ROLES set rol='{rol.getRol()}' "
        con.ejecuta_query(sql)
        con.commit()
        input("\n Datos Ingresados Correctamente...")
        #Cierra la conexion hacia la base de datos
        con.desconectar()
    except pymysql.MySQLError as e:
        print(e)


def update(rol):
    try:
        #Abre la conexion hacia la base de datos
        con=Conexion(host,user,password,db)
        sql=f"UPDATE ROLES SET rol='{rol.getRol()}' WHERE id_rol={rol.getId()}"
        con.ejecuta_query(sql)
        con.commit()
        input("\n Datos Actualizados Correctamente...")
        #Cierra la conexion hacia la base de datos
        con.desconectar()
    except pymysql.MySQLError as e:
        print(e)

def BuscarId(id):
    try:
        con=Conexion(host,user,password,db)
        sql=f"Select * from roles where id_rol={id}"
        cursor=con.ejecuta_query(sql)
        datos=cursor.fetchone() #trae un solo registro
        con.desconectar()
        return datos
    except pymysql.MySQLError as e:
        con.rollback() #Volver al paso anterior de ejecutar la sentencia
        print(e)

def BuscarPorRol(rol):
    try:
        con=Conexion(host,user,password,db)
        sql=f"Select id from roles where rol={rol}"
        cursor=con.ejecuta_query(sql)
        datos=cursor.fetchone() #trae un solo registro
        con.desconectar()
        return datos
    except pymysql.MySQLError as e:
        con.rollback() #Volver al paso anterior de ejecutar la sentencia
        print(e)

def remove(id):
    try:
        #Abre la conexion hacia la base de datos
        con=Conexion(host,user,password,db)
        sql=f"DELETE FROM ROLES WHERE id_rol={id}"
        con.ejecuta_query(sql)
        con.commit()
        input("\n Producto Eliminado Correctamente...")
        #Cierra la conexion hacia la base de datos
        con.desconectar()
    except pymysql.MySQLError as e:
        print(e)

def Listar():
    try:
        con=Conexion(host,user,password,db)
        sql="Select * from roles"
        cursor=con.ejecuta_query(sql)
        datos=cursor.fetchall() #trae un conjunto de filas
        con.desconectar()
        return datos
    except pymysql.MySQLError as e:
        con.rollback() #Volver al paso anterior de ejecutar la sentencia
        print(e)