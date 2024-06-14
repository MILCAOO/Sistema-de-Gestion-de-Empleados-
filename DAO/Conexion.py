import pymysql

class Conexion:

    #Creamos el constructor
    def __init__(self,host,user,password,db)->None:
        #Crea la conexion a la base de datos
        self.db=pymysql.connect(host=host,user=user,password=password,db=db)
        self.cursor=self.db.cursor()

    def ejecuta_query(self,sql):
        try:
            self.cursor.execute(sql)
            return self.cursor
        except pymysql.MySQLError as e:
            print(f"Error en Comando SQL:  {e}")


    def desconectar(self):
        try:
            self.db.close()
        except pymysql.MySQLError as e:
            print(f"Error cerrando Conexion:  {e}")

    def commit(self):
        try:
            self.db.commit()
        except pymysql.MySQLError as e:
            print(f"No se puede confirmar accion:  {e}")
    
    def rollback(self):
        try:
            self.db.rollback()
        except pymysql.MySQLError as e:
            print(f"No se puede ejecturar el Rollback:  {e}")