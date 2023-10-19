from ExpenseController import ExpenseController
from UserController import UserController
from User import User


class SplitwiseDriver:

    def printStatement(self, statements):
        for s in statements:
            print(s)

    def main(self):
        expenseList = list()
        userList = list()

        u1 = User("u1", 1)
        userList.append(u1)
        u2 = User("u2", 2)
        userList.append(u2)
        u3 = User("u3", 3)
        userList.append(u3)
        u4 = User("u4", 4)
        userList.append(u4)
        userManager = UserController(userList)

        ex1 = ExpenseController(u1, 1000, 4, [u1, u2, u3, u4], "EQUAL", [])

        # self.printStatement(userManager.getUserBill(u4))
        # self.printStatement(userManager.getUserBill(u1))

        ex2 = ExpenseController(u1, 1250, 2, [u2, u3], "EXACT", [370, 880])
        # self.printStatement(ex2.getSettledBill())

        ex3 = ExpenseController(u4, 1200, 4, [u1, u2, u3, u4], "PERCENT", [40, 20, 20, 20])
        self.printStatement(userManager.getUserBill(u1))
        # self.printStatement(ex3.getSettledBill())


spl = SplitwiseDriver()
spl.main()
