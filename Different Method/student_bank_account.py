import kuwait_bank


acc_type = ["checking", "saving"]
student_bank_account = []
transaction_detail=[]


def add_student_account():  
    new_student = kuwait_bank.Student("abdu", 22416, 282808, 90, "saving")
    student_bank_account.append(new_student)
    new_student = kuwait_bank.Student("faizal", 24516, 281008, 45, "checking")

    student_bank_account.append(new_student)
    new_student = kuwait_bank.Student("shaikh", 22656, 283808, 50, "saving")
    student_bank_account.append(new_student)
    new_student = kuwait_bank.Student("suhail", 24917, 182808, 67, "checking")
    student_bank_account.append(new_student)
    new_student = kuwait_bank.Student("majid", 25510, 682808, 77, "saving")
    student_bank_account.append(new_student)


def add_transactions():
    for i in range(len(student_bank_account)):
        new_transaction=kuwait_bank.Transaction(student_bank_account[i].name,student_bank_account[i].id,student_bank_account[i].accountNum,student_bank_account[i].balance,student_bank_account[i].type)
        transaction_detail.append(new_transaction)
    for i in range(len(transaction_detail)):
        transaction_detail[i].deposit(50)
        transaction_detail[i].withdraw(30)

def perform_transactions():
    account_num=int(input("Enter Account Number: "))
    for i in range(len(transaction_detail)):
      if account_num==transaction_detail[i].accountNum:
        transaction_detail[i].display_transaction()
        print('--------------------------------------------------------------------------------------------------------------')
        print("1-Deposite\t2-Withdrow\t3-Activate\t4-Deactivate")
        choice=int(input("Enter Your Choice: "))
        if choice==1:
            depo=int(input("Enter Deposit Amount: "))
            transaction_detail[i].deposit(depo)
        elif choice==2:
            depo=int(input("Enter Withdraw Amount: "))
            transaction_detail[i].withdraw(depo)
        elif choice==3:
            transaction_detail[i].activate_account()
        elif choice==4:
            transaction_detail[i].deactivate_account()
        else:
            print("Please Choose Valid Option")


def print_student_info():
    for i in range(len(student_bank_account)):
        student_bank_account[i].display_account_info()


def print_student_balance():
    for i in range(len(student_bank_account)):
        student_bank_account[i].display_student_balance()


def new_add_student():
    print("Please Enter New Student Information:")
    print("--------------------------------------")
    name = input("Please Enter Student Name: ")
    for i in range(len(student_bank_account)):
        if (student_bank_account[i].name.find(name) > -1):
            print("Please Enter Unique Student Name")
            name = input("Please Enter Student Name: ")
            continue
        else:
            pass
    id = int(input("Please Enter Student ID: "))
    for i in range(len(student_bank_account)):
        if id==student_bank_account[i].id:
            print("Please Enter Unique Id Number")
            id = int(input("Please Enter Student Id Number: "))
            continue
        else:
            pass
    accountNum = int(input("Please Enter Student Account Number: "))
    for i in range(len(student_bank_account)):
        if accountNum==student_bank_account[i].accountNum:
            print("Please Enter Unique Account Number")
            accountNum = int(input("Please Enter Student Account Number: "))
            continue
        else:
            pass
    print("1-Checking Account\t\t2-Saving Account")
    choose = int(input("Which Type Of Account You Choose? "))
    type = acc_type[choose-1]
    balance = int(input("Plase Enter Balance: "))
    for i in range(len(student_bank_account)):
        if type==acc_type[0]:
            if balance<=1:
                print("1 KD or More for Checking Account")
                balance = int(input("Plase Enter Balance: "))
                continue
            else:
                pass
        else:
            if balance<=10:
                print("10 KD or More for Saving Account")
                balance = int(input("Plase Enter Balance: "))
                continue
            else:
                pass
    new_student = kuwait_bank.Student(name, id, accountNum, balance, type)
    new_transaction = kuwait_bank.Transaction(name, id, accountNum, balance, type)
    student_bank_account.append(new_student)
    transaction_detail.append(new_transaction)


def search_bank_account_by_name():
    name = input("Please Enter Name: ")
    for i in range(len(student_bank_account)):
        if (student_bank_account[i].name.find(name) > -1):
            student_bank_account[i].display_account_info()


def print_student_transaction():
    for i in range(len(transaction_detail)):
        transaction_detail[i].display_transaction()


def show_menu():
    print('--------------------------------------------------------------------------------------------------------------')
    print("Select an item from the menu:")
    print("1-Add New Student Account")
    print("2-Perform Transaction on Accounts")
    print("3-Show All Student Account Balance")
    print("4-Show All Student Account")
    print("5-Search Student Account By Name")
    print("6-Display Transactions for a Students")
    print("0-Exit")
    print('--------------------------------------------------------------------------------------------------------------')


add_student_account()
add_transactions()
for i in range(10000):
    show_menu()
    result = int(input("What is your choice: "))
    if result == 0:
        break
    elif result == 1:
        new_add_student()
    elif result == 2:
        perform_transactions()
    elif result == 3:
        print_student_balance()
    elif result == 4:
        print_student_info()
    elif result == 5:
        search_bank_account_by_name()
    elif result == 6:
        print_student_transaction()
