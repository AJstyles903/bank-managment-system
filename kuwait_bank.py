class Student:
    def __init__(self, name, id, accountNum, balance, type):
        self.name = name
        self.id = id
        self.accountNum = accountNum
        self.balance = balance
        self.type = type
        self.status = "Active"
        self.deposit_history = []
        self.withdraw_history = []
        

    def display_account_info(self):
        print('--------------------------------------------------------------------------------------------------------------')
        print("Student Name: ", self.name, ", Balance: ", self.balance, ", Account Number: ",self.accountNum, ", Student ID: ", self.id, ", Account type: ", self.type)

    def display_student_balance(self):
        print('--------------------------------------------------------------------------------------------------------------')
        print("Student Name: ", self.name, ", Balance: ", self.balance)

    def activate_account(self):
        self.status = "Active"
        print("Account has been activated")
        print()

    def deactivate_account(self):
        self.status = "Not Active"
        print("Account has been deactivated")
        print()

    def deposit(self, deposit):
        self.balance =self.balance+ deposit
        self.deposit_history.append(deposit)
        print(deposit," has been deposited")

    def withdraw(self, withdraw):
        if self.status == "Active":
            if self.type=="checking":
                if self.balance-withdraw<=1:
                    print("1 KD or more balance")
                elif self.balance < withdraw:
                    print("Sorry, insufficient funds")
                else:
                    self.balance -= withdraw
                    self.withdraw_history.append(withdraw)
                    print(withdraw, " has been withdrawn")
            elif self.type=="saving":
                if self.balance-withdraw<=10:
                    print("Must be 10 KD or more balance")
                elif self.balance < withdraw:
                    print("Sorry, insufficient funds")
                else:
                    self.balance -= withdraw
                    self.withdraw_history.append(withdraw)
                    print(withdraw, " has been withdrawn")
        else:
            print("Sorry, Account it NOT ACTIVE")

    def display_transaction(self):
        print('--------------------------------------------------------------------------------------------------------------')
        print("Student Name: ",self.name,", Account Number: ",self.accountNum,", Balance: ",self.balance,", Deposits: ", self.deposit_history,", Withdraws: ", self.withdraw_history)