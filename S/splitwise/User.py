class User:
    __name = None 
    __dues = None 
    __id = None

    def __init__(self,name,id):
        self.__id= id 
        self.__name= name 
        self.__dues= dict()

    def getName(self):
        return self.__name
    
    def getId(self):
        return self.__id
    
    def getDebts(self):
        return self.__dues
    
    
