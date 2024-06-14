from DAO.Conexion import Conexion
from DTO.Departamento import Departamento
import pymysql

host='localhost'
user="root"
password=''
db='empresa'

def add(departamento):
    try:
        #Abre la conexion hacia la base de datos
        con=Conexion(host,user,password,db)
        sql=f"INSERT INTO DEPARTAMENTO set nombre_departamento='{departamento.getNombreDepartamento()}' "
        con.ejecuta_query(sql)
        con.commit()
        input("\n Datos Ingresados Correctamente...")
        #Cierra la conexion hacia la base de datos
        con.desconectar()
    except pymysql.MySQLError as e:
        print(e)


def update(departamento):
    try:
        #Abre la conexion hacia la base de datos
        con=Conexion(host,user,password,db)
        sql=f"UPDATE DEPARTAMENTO SET nombre_departamento='{departamento.getNombreDepartamento()}' WHERE id_departamento='{departamento.getIdDepartamento()}' "
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
        sql=f"Select * from departamento where id_departamento={id}"
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
        sql=f"DELETE FROM DEPARTAMENTO WHERE id_departamento={id}"
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
        sql="Select * from departamento"
        cursor=con.ejecuta_query(sql)
        datos=cursor.fetchall() #trae un conjunto de filas
        con.desconectar()
        return datos
    except pymysql.MySQLError as e:
        con.rollback() #Volver al paso anterior de ejecutar la sentencia
        print(e)