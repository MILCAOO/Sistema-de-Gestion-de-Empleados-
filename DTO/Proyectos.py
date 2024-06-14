class Proyectos:
    __id=0
    __nombre=""
    __descripcion=""
    __fechainicio=""

    def __init__(self,nombre,descripcion,fechainicio)->None:
        self.__nombre=nombre
        self.__descripcion=descripcion
        self.__fechainicio=fechainicio
    
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nombre):
        self.__nombre=nombre

    def getDescripcion(self):
        return self.__descripcion
    def setDescripcion(self,descripcion):
        self.__descripcion=descripcion

    def getFechainicio(self):
        return self.__fechainicio
    def setFechainicio(self,fechainicio):
        self.__fechainicio=fechainicio
    
    def getId(self):
        return self.__id
    def setId(self,id):
        self.__id=id