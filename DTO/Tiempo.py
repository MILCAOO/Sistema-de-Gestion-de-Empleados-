class Tiempo:
    
    
    __id=0
    __horas=""
    __tareas=""
    __fecha=""
    __descripcion="" 
    
    
    def __init__(self,horas,tareas,fecha,descripcion)->None:
        self.__horas=horas
        self.__tareas=tareas
        self.__fecha=fecha
        self.__descripcion=descripcion
        
        
    def setId(self,id):
        self.__id=id
        
    def sethoras(self,horas):
        self.__horas=horas
        
    def settareas(self,tareas):
        self.__tareas=tareas
        
    def setfecha(self,fecha):
        self.__fecha=fecha
    
    def setdescripcion(self,descripcion):
        self.__descripcion=descripcion
        
        
        
    def getId(self):
        return self.__id
    
    def getHoras(self):
        return self.__horas
    
    def getTareas(self):
        return self.__tareas
    
    def getFecha(self):
        return self.__fecha
    
    def getDescripcion(self):
        return self.__descripcion