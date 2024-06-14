from DAO.Conexion import Conexion
from DTO.Empleados import Empleados
import pymysql

host='localhost'
user="root"
password=''
db='empresa'

def add(empleado):
    try:
        #Abre la conexion hacia la base de datos
        con=Conexion(host,user,password,db)
        sql=f"INSERT INTO EMPLEADOS set nombre_empleado='{empleado.getNombreEmpleado()}', direccion='{empleado.getDireccion()}', fono='{empleado.getFono()}', correo='{empleado.getCorreo()}', fecha_contrato='{empleado.getFechacontrato()}', salario='{empleado.getSalario()}' "
        con.ejecuta_query(sql)
        con.commit()
        input("\n Datos Ingresados Correctamente...")
        #Cierra la conexion hacia la base de datos
        con.desconectar()
    except pymysql.MySQLError as e:
        print(e)


def update(empleado):
    try:
        #Abre la conexion hacia la base de datos
        con=Conexion(host,user,password,db)
        sql=f"UPDATE empleados SET nombre_empleado='{empleado.getNombreEmpleado()}', direccion='{empleado.getDireccion()}', fono='{empleado.getFono()}', correo='{empleado.getCorreo()}', fecha_contrato='{empleado.getFechacontrato()}', salario='{empleado.getSalario()}' WHERE id_empleado={empleado.getIdEmpleado()} "
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
        sql=f"Select * from empleados where id_empleado={id}"
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
        sql=f"DELETE FROM EMPLEADOS WHERE id_empleado={id}"
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
        sql="Select * from empleados"
        cursor=con.ejecuta_query(sql)
        datos=cursor.fetchall() #trae un conjunto de filas
        con.desconectar()
        return datos
    except pymysql.MySQLError as e:
        con.rollback() #Volver al paso anterior de ejecutar la sentencia
        print(e)