from Expense import Expense


class ExpenseController:
    __expense= None
    __settledBill = None
    def __init__(self,paiby,amount,divisions, debtUsers,strategy,contributions):
        self.__settledBill= list()
        self.__expense = Expense(paiby,amount,divisions, debtUsers,strategy,contributions)
        self.__settleBill()
        
    
    def __settleBill(self):
        bill = self.__expense.getBill()
        
        for b in bill:
            gu,du = b[0],b[1]
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
                
