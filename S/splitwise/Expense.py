from CalculationService import CalculationService


class Expense:

    __paidBy = None 
    __amount = None 
    __divisions = None 
    __debtUsers = None 
    __strategy = None 
    __contributions = None
    __bill = None 
    calculation = CalculationService()

    def __init__(self,paiby,amount,divisions, debtUsers,strategy,contributions):
        self.__paidBy = paiby
        self.__amount = amount 
        self.__divisions = divisions
        self.__debtUsers = debtUsers
        self.__strategy = strategy
        self.__contributions = contributions
        self.__bill = list()
        
    
    def getBill(self):

        if self.__strategy=="PERCENT":
            self.__bill = self.calculation.percentageSplit(self.__paidBy,self.__amount,self.__debtUsers,self.__contributions)
        elif self.__strategy=="EXACT":
            self.__bill = self.calculation.exactSplit(self.__paidBy,self.__amount,self.__debtUsers,self.__contributions)
        elif self.__strategy=="EQUAL":
            self.__bill = self.calculation.equalSplit(self.__paidBy,self.__amount,self.__debtUsers,self.__contributions)
        return self.__bill 
    
    def getPaidBy(self):
        return self.__paidBy
    
    def getDeptUsers(self):
        return self.__debtUsers