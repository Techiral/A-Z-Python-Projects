import abc
class CalcultaionServiceImpl(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def percentageSplit(paidby,amount,debtusers,contributions):
        pass 

    @abc.abstractmethod
    def equalSplit(paidby,amount,debtusers,contributions):
        pass 

    @abc.abstractmethod
    def exactSplit(paidby,amount,debtusers,contributions):
        pass 


    