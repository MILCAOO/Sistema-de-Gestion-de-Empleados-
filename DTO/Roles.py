class Roles:

    __id=0
    __rol=""

    def __init__(self,rol)->None:
        self.__rol=rol

    def getRol(self):
        return self.__rol
    def setRol(self,rol):
        self.__rol=rol
    
    def getId(self):
        return self.__id
    def setId(self,id):
        self.__id=id