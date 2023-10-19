class UserController:
    __userList= None
    __settledBill = None
    def __init__(self,userList):
        self.__settledBill= list()
        self.__userList = userList
        self.__settleBill()
        
    
    def __settleBill(self):
        for gu in self.__userList:
            for du in self.__userList:
                if (gu!=du):
                    if (du.getDebts().get(gu,0)>gu.getDebts().get(du,0)):
                        du.getDebts()[gu] = du.getDebts().get(gu,0) - gu.getDebts().get(du,0)
                        gu.getDebts()[du] = 0
                        updateString = gu.getName() + " pays " + str(du.getDebts()[gu]) + "to " + du.getName()
                        self.__settledBill.append(updateString)
                    elif (du.getDebts().get(gu,0)<gu.getDebts().get(du,0)):
                        gu.getDebts()[du] = gu.getDebts().get(du,0) - du.getDebts().get(gu,0) 
                        du.getDebts()[gu] = 0
                        updateString = du.getName() + " pays " + str(gu.getDebts()[du]) + "to " + gu.getName()
                        self.__settledBill.append(updateString)
                    else:
                        gu.getDebts()[du] = gu.getDebts().get(du,0) - du.getDebts().get(gu,0) 
                        du.getDebts()[gu] = 0
                
    def getSettledBill(self):
        return self.__settledBill
    
    def getUserBill(self,u):
        self.getSettledBill()
        userBill = list()
        for gu in self.__userList:
            if (gu!=u):
                if (u.getDebts().get(gu,0)>gu.getDebts().get(u,0)):
                    updateString = gu.getName() + " pays " + str(u.getDebts()[gu]) + "to " + u.getName()
                    userBill.append(updateString)
                elif (u.getDebts().get(gu,0)<gu.getDebts().get(u,0)):
                    u.getDebts()[gu] = 0
                    updateString = u.getName() + " pays " + str(gu.getDebts()[u]) + "to " + gu.getName()
                    userBill.append(updateString)
        if (len(userBill)==0):
            userBill.append("No Bill ")
        return userBill
