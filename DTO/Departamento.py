class Departamento:

    __iddepartamento=0
    __nombredepartamento=""

    def __init__(self,nombredepartamento)->None:
        self.__nombredepartamento=nombredepartamento
    
    def getNombreDepartamento(self):
        return self.__nombredepartamento
    def setNombreDepartamento(self,nombredepartamento):
        self.__nombredepartamento=nombredepartamento


    def getIdDepartamento(self):
        return self.__iddepartamento
    def setIdDepartamento(self,id):
        self.__iddepartamento=id