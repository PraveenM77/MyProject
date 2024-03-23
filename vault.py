import random
class Vault:
    def __init__(self,name,balance):
        self.balance=balance
        self.isOpen=False
        self.name=name
        self.password="1234"

    def openVault(self):
        user_id=input("Enter User ID : ")
        password=input("Enter Password : ")
        while user_id!=self.name or password!="1234":
            print("You have entered Wrong User ID or Password. Please Enter Correct UserID or Password")
            ur_choice=input("Do you want to try again!. Please enter Yes or No :")
            if ur_choice=="Yes":
                user_id=input("Enter User ID : ")
                password=input("Enter Password : ")
            else:
                break
        else:
            self.isOpen=True
            print("Account is Opened")
        return True
    
    def addCashToVault(self,cash):
        if self.isOpen==False:
            return "Vault is not opened. Please open it."
        else:
            self.balance += cash
            return cash

        
    def closeVault(self):
        if self.isOpen==True:
            self.isOpen=False
        return f"Your Account is Closed by {self.name}"

    
    def removeCashFromVault(self,cash):
        if self.isOpen==False:
            return "Vault is not opened. Please open it."
        else:
            self.balance -= cash
            return cash
        
    def getBalance(self):
        return self.balance
#****************************************************************************************************************************************************    
class BankManager(Vault):
    def __init__(self,name,cashBalance):
        super().__init__(name,cashBalance)
        self.cashBalance=cashBalance
        self.name=name

    def addCashToCashier(self,cash,noOfCashier):
        if 0<cash<=self.cashBalance:
            self.cashBalance -= cash
            amount=cash//noOfCashier
            return amount
        elif cash>self.cashBalance:
            return "insufficient Balance"
        
    def getCashFromCashier(self,cash):
        if cash>0:
            self.cashBalance +=cash
            return cash
        else:
            return "Enter a correct amount"
    
        
    def getBalance(self):
        return super().getBalance()
        

#****************************************************************************************************************************************************
class Cashier(Vault):
    def __init__(self,name,balance):
        super().__init__(name,balance)
        self.balance=balance
        self.name=name
        isOpen=False
        
    def receiveCashFromManager(self,amount):
        self.balance += amount
        return amount
    
    def giveCashToCustomer(self,amount):
        if 0<amount<self.balance:
            self.balance -= amount
            return amount
    
    def receiveCashFromCustomer(self,amount):
        if amount>0:
            self.balance += amount
            
    def getBalance(self):
        return self.balance
    
    def sendCashToBankManager(self):
        return self.balance

#****************************************************************************************************************************************************
        
class Customer():
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance=self.balance+amount
            return amount
        else:
            print("Enter Correct Amount")
    def withdraw(self,amount):
        if self.balance>amount>0:
            self.balance -= amount
            return amount
        else:
            print("Insufficient Balance")
    def getBalance(self):
        return self.balance
#****************************************************************************************************************************************************

print("Bank To Cashier Portal")

v=Vault("shiva",500000)
b=BankManager("shiva",v.getBalance())
cashierA=Cashier("CashierA",0)
cashierB=Cashier("CashierB",0)
cashierC=Cashier("CashierC",0)
cashierD=Cashier("CashierD",0)

while True:
    ur_choice=int(input(""""Enter Your Choice : 
                        1. openVault
                        2. addCashToCashier
                        3. getCashFromCashier
                        4. getBalance of Bank Manager Account
                        5. Cashier & Customer Transaction
                        6. Exit
                        : """))
    if ur_choice==1:
        b.openVault()
    elif ur_choice==2:
        amount=int(input("Enter a amount to transfer cashier"))
        noOfCashier=int(input("Enter no Of Cashier"))
        result=b.removeCashFromVault(amount)
        if result!="Vault is not opened. Please open it.":
            a=b.addCashToCashier(result,noOfCashier)
            print(f"Bank Manager Transfering Amount {result} and Each Cashier Getting {a}")
            print(b.closeVault())
            print("CashierA received Cash From Manager",cashierA.receiveCashFromManager(a))
            print("CashierB received Cash From Manager",cashierB.receiveCashFromManager(a))
            print("CashierC received Cash From Manager",cashierC.receiveCashFromManager(a))
            print("CashierD received Cash From Manager",cashierD.receiveCashFromManager(a))
            
        else:
            print(result)
    elif ur_choice==3:
        amount=cashierA.sendCashToBankManager()
        print(amount)
        result=b.getCashFromCashier(amount)
        a=b.addCashToVault(result)
        if a!="Vault is not opened. Please open it.":
            print("Vault has recieved cash from cashier",a)
            print(b.closeVault())
        else:
            print(a)
    elif ur_choice==4:
        print(b.getBalance())
                
    else:
        break



#****************************************************************************************************************************************************

print("Cashier and Customer Transaction")

while True:
    cashiers = {
        "cashierA": cashierA,
        "cashierB": cashierB,
        "cashierC": cashierC,
        "cashierD": cashierD
        }

    customer_account_no=int(input("Enter Customer Account Number"))


    customers = {
            10001:["Ravi",0],
            10002:["Arun",0],
            10003:["Sujay",0],
            10004:["Ramesh",0],
            10005:["Bhanu",0],
            10006:["Arya",0]
            }

    for k,v in customers.items():
        if customer_account_no==k:
            print("Hello ",customers[k][0])
            selected_cashier_name = random.choice(list(cashiers.keys()))
            print("Please Contact ", selected_cashier_name)
            ur_choice=int(input("Enter Your Choice 1. Deposit 2. Withdraw "))
            print("customer name",customers[k][0])
            customer_name=Customer(customers[k][1])
            selected_cashier=cashiers[selected_cashier_name]
            if ur_choice==1:
                amount=int(input("Enter amount"))
                print(customer_name.deposit(amount))
                print("Total Amount is",customer_name.getBalance())
                selected_cashier.receiveCashFromCustomer(amount)
                print(selected_cashier_name ,"Balance",selected_cashier.getBalance())
                break
            elif ur_choice==2:
                amount=int(input("Enter amount"))
                print(customer_name.withdraw(amount))
                print("Total Amount is",customer_name.getBalance())
                selected_cashier.giveCashToCustomer(amount)
                print(selected_cashier_name ,"Balance",selected_cashier.getBalance())
                break
        else:
            print("You dont have bank account")
            break
    ur_choice=input("Enter Your Choice")
    if ur_choice=="No":
        break
    


