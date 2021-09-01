class ATM(object):
    def __init__(self, name, amount, pin, cnumber, rnumber):
        self.name = name
        self.amount = int(amount)
        self.pin = pin
        self.cnumber = cnumber
        self.rnumber = rnumber

    def doWithdraw(self):
        withdrawAmount = int(input("Please Add Amount To Be Withdrawn: "))
        if (withdrawAmount<=self.amount):
            self.amount = self.amount - withdrawAmount
            return self.amount
        else :
            print("Insufficient Funds")
            withdraw = self.doWithdraw()

    def doDeposit(self):
        depositAmount = int(input("Please Add Amount To Be Deposited: "))
        if (depositAmount<=100000 and depositAmount>=1):
            self.amount = self.amount + depositAmount
            return self.amount
        else :
            print("Error In Transaction")
            deposit = self.doDeposit()
    
    def balanceInquiry(self):
        print(f"Your balance is {self.amount}")
        
    def transactions(self):
        action=int(input("What would you like to do ((1=withdraw)(2=deposit)(3=balance)(4=exit)): "))
        if (action==1):
            withdraw = self.doWithdraw()
            print(f"Your new balance is {self.amount}!")
            t=self.transactions()
        elif (action==2):
            deposit = self.doDeposit()
            print(f"Your new balance is {self.amount}!")
            t=self.transactions()
        elif (action==3):
            balance = self.balanceInquiry()
            t=self.transactions()
        elif (action==4):
            print("Bye")
        else :
            print("Please Enter A Valid Action")
            t=self.transactions()

# Define some accounts
account1 = ATM('John',10000,7231,349417460193,193660472)

# Now we can define amounts
account1.transactions()
 