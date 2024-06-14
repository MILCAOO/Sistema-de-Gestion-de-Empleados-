from DAO.Conexion import Conexion
from DTO.Tiempo import Tiempo
import pymysql

host='localhost'
user="root"
password=''
db='empresa'

def add(tiempo):
    try:
        #Abre la conexion hacia la base de datos
        con=Conexion(host,user,password,db)
        sql=f"INSERT INTO TIEMPO set horas='{tiempo.getHoras()}', tareas='{tiempo.getTareas()}', fecha='{tiempo.getFecha()}', descripcion='{tiempo.getDescripcion()}' "
        con.ejecuta_query(sql)
        con.commit()
        input("\n Datos Ingresados Correctamente...")
        #Cierra la conexion hacia la base de datos
        con.desconectar()
    except pymysql.MySQLError as e:
        print(e)
        
def update(Tiempo):
    try:
        #Abre la conexion hacia la base de datos
        con=Conexion(host,user,password,db)
        sql=f"UPDATE TIEMPO SET horas='{Tiempo.getHoras()}', tareas='{Tiempo.getTareas()}' , fecha='{Tiempo.getFecha()}' , descripcion='{Tiempo.getDescripcion()}'  WHERE id_tiempo={Tiempo.getId()}"
        con.ejecuta_query(sql)
        con.commit()
        input("\n Datos Actualizados Correctamente...")
        #Cierra la conexion hacia la base de datos
        con.desconectar()
    except pymysql.MySQLError as e:
        print(e)
        
def remove(id):
    try:
        #Abre la conexion hacia la base de datos
        con=Conexion(host,user,password,db)
        sql=f"DELETE FROM TIEMPO WHERE id_tiempo={id}"
        con.ejecuta_query(sql)
        con.commit()
        input("\n Eliminado Correctamente...")
        #Cierra la conexion hacia la base de datos
        con.desconectar()
    except pymysql.MySQLError as e:
        print(e)
        

def BuscarId(id):
    try:
        con=Conexion(host,user,password,db)
        sql=f"Select * from tiempo where id_tiempo={id}"
        cursor=con.ejecuta_query(sql)
        datos=cursor.fetchone() #trae un solo registro
        con.desconectar()
        return datos
    except pymysql.MySQLError as e:
        con.rollback() #Volver al paso anterior de ejecutar la sentencia
        print(e)
        
        
