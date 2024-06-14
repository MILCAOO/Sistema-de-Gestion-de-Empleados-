class Empleados:
    
    __idempleado=0
    __nombreempleado=""
    __direccion=""
    __fono=""
    __correo=""
    __fechacontrato=""
    __salario=""



    def __init__(self,nombreempleado,direccion,fono,correo,fechacontrato,salario)->None:
        self.__nombreempleado=nombreempleado
        self.__direccion=direccion
        self.__fono=fono
        self.__correo=correo
        self.__fechacontrato=fechacontrato
        self.__salario=salario


    def getIdEmpleado(self):
        return self.__idempleado
    def setIdEmpleado(self,idempleado):
        self.__idempleado=idempleado
        
    def getNombreEmpleado(self):
        return self.__nombreempleado
    def setNombreEmpleado(self,nombreempleado):
        self.__nombreempleado=nombreempleado

    def getDireccion(self):
        return self.__direccion
    def setDireccion(self,direccion):
        self.__direccion=direccion
    
    def getFono(self):
        return self.__fono
    def setFono(self,fono):
        self.__fono=fono
    
    def getCorreo(self):
        return self.__correo
    def setCorreo(self,correo):
        self.__correo=correo

    def getFechacontrato(self):
        return self.__fechacontrato
    def setFechacontrato(self,fechacontrato):
        self.__fechacontrato=fechacontrato
    
    def getSalario(self):
        return self.__salario
    def setSalario(self,salario):
        self.__salario=salario
    