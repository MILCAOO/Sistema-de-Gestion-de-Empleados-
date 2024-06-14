from DAO.Conexion import Conexion
from DTO.Empleados import Empleados
import pymysql

host='localhost'
user="root"
password=''
db='empresa'

  
def Asignar_empleado_a_departamento(id_empleado, id_departamento):
    try:
        con=Conexion(host,user,password,db)
        sql = f"INSERT INTO EmpleadoDepartamento (id_empleado, id_departamento) VALUES ({id_empleado}, {id_departamento})"
        con.ejecuta_query(sql)
        con.commit()
        print("Empleado asignado al departamento correctamente.")
    except pymysql.MySQLError as e:
            print("Error al asignar empleado al departamento:", e)
            
            
            
def BuscarId(id):
    try:
        con=Conexion(host,user,password,db)
        sql=f"Select * from empleadodepartamento where id={id}"
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
        sql=f"DELETE FROM empleadodepartamento WHERE id={id}"
        con.ejecuta_query(sql)
        con.commit()
        input("\n Eliminado Correctamente...")
        #Cierra la conexion hacia la base de datos
        con.desconectar()
    except pymysql.MySQLError as e:
        print(e)

def update(id_reasignacion, id_empleado, id_departamento):
    try:
        #Abre la conexion hacia la base de datos
        con=Conexion(host,user,password,db)
        sql = f"UPDATE EmpleadoDepartamento SET id_empleado={id_empleado}, id_departamento={id_departamento} WHERE id={id_reasignacion}"
        con.ejecuta_query(sql)
        con.commit()
        input("\n Datos Actualizados Correctamente...")
        #Cierra la conexion hacia la base de datos
        con.desconectar()
    except pymysql.MySQLError as e:
        print(e)