class Usuario:
    __username=''
    __password_hash=''
    __rol=""
    
    def __init__(self,username,password_hash,rol):
        self.__username=username
        self.__password_hash=password_hash
        self.__rol=rol
    def getUsername(self):
        return self.__username
    def getPassword_Hash(self):
        return self.__password_hash
    def getRol(self):
        return self.__rol
