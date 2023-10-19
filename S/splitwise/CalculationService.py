from CalculationServiceImp import CalcultaionServiceImpl


class CalculationService(CalcultaionServiceImpl):

    def percentageSplit(self, paidby, amount, debtusers, contributions):
        billCopy = list()
        for i in range(len(debtusers)):
            c = (contributions[i] * amount) / 100
            paidby.getDebts()[debtusers[i]] = paidby.getDebts().get(debtusers[i], 0) + c
            billCopy.append((paidby, debtusers[i], c))
        return billCopy

    def equalSplit(self, paidby, amount, debtusers, contributions):
        billCopy = list()
        for i in range(len(debtusers)):
            c = (amount) / len(debtusers)
            paidby.getDebts()[debtusers[i]] = paidby.getDebts().get(debtusers[i], 0) + c
            billCopy.append((paidby, debtusers[i], c))
        return billCopy

    def exactSplit(self, paidby, amount, debtusers, contributions):
        billCopy = list()
        for i in range(len(debtusers)):
            c = contributions[i]
            paidby.getDebts()[debtusers[i]] = paidby.getDebts().get(debtusers[i], 0) + c
            billCopy.append((paidby, debtusers[i]))
        return billCopy
