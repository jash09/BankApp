from account import Account
from bank import Bank

class Customer:
    customerId = -1
    allCustomer = []
    def __init__(self, firstNAme, lastName, username):
        self.firstNAme = firstNAme
        self.Lastname = lastName
        self.totalBalance = 0
        self.username = username
        self.customerId = Customer.customerId
        self.accounts = []

    @staticmethod
    def findCustomer(username):
        for u in Customer.allCustomer:
            if u.username == username:
                return True, u
        return False, None


    @staticmethod
    def createNewCustomer(firstName, lastName, username):
        doesCustomerExist, customer = Customer.findCustomer(username)
        if doesCustomerExist:
            return False, "Username already exists"
        Customer.customerId += 1
        newCustomer = Customer(firstName, lastName, username)
        Customer.allCustomer.append(newCustomer)
        return Customer(firstName, lastName, username)
    
    def deposit(self, amount, bankAbbreviation):
        doesAccountExists, account = self.findAccount(bankAbbreviation)
        if not doesAccountExists:
            return False, "Account not present"
        account.balance += amount
        self.__updateTotalBalance()
        self.displayBalance(bankAbbreviation)
        return True, "Deposit Successful"
    
    def withdraw(self, amount, bankAbbreviation):
        isAccountExists, account = self.findAccount(bankAbbreviation)
        if not isAccountExists:
            return False, "Account not present"
        #check balance is sufficient
        if not account.isSufficientBalance(amount):
            return False, "Insufficient Balance"
        account. balance -= amount
        self.__updateTotalBalance()
        self.displayBalance(bankAbbreviation)
        return True, "Withdraw successful"

    def transferAmount(self, creditCustomerUsername, creditbankAbbreviation, debitbankAbbreviation, amount):
    
        iscreditCustomerExists, creditCustomer = Customer.findCustomer(creditCustomerUsername)
        if not iscreditCustomerExists:
            return False, "Customer not present"
        
        isAmountWithdrawn, message = self.withdraw(amount, debitbankAbbreviation)
        if not isAmountWithdrawn:
            return False, "Insufficient Balance"
        
        isAmountCredited, message = creditCustomer.deposit(amount, creditbankAbbreviation)
        if not isAmountCredited:
            self.deposit(amount, debitbankAbbreviation)
            return False, "Account not found"
        
        return True, "Amount Transferred"
    
    def selfTransfer(self, creditbankAbbr, amount, debitbankAbbr):
        isAmountWithdrawn, message = self.withdraw(amount, debitbankAbbr)
        if not isAmountWithdrawn:
            return False, "Insufficient Balance"
        
        isAmountCredited, message = self.deposit(amount, creditbankAbbr)
        if not isAmountCredited:
            self.deposit(amount, debitbankAbbr)
            return False, "Not possible"
        return True, "Amount Transferred"


    def findAccount(self, bankAbbreviation):
        if (len(self.accounts) == 0):
            return False, "No accounts found"
        for a in self.accounts:
            if a.isAccountExist(bankAbbreviation):
                return True, a
        return False, None

    def __updateTotalBalance(self):
        self.totalBalance = 0
        for a in self.accounts:
            self.totalBalance += a.balance
    
    def displayTotalBalance(self):
        print(self.firstNAme, self.totalBalance)
    
    def displayBalance(self, bankAbbreviation):
        for a in self.accounts:
            if a.bank.bankAbbreviation == bankAbbreviation:
                print(self.firstNAme,'balance in', a.bank.fullName,'is', a.balance)
                return True, "Account Balance displayed"
        return False, "Wrong bankAbbreviation given"

    def createNewAccount(self, bankAbbreviation):
        isAccountExist, account = self.findAccount(bankAbbreviation)
        if isAccountExist:
            return False, "Your Account already exist"
        isAccountCreated, account = Account.createNewAccount(bankAbbreviation)
        if not isAccountCreated:
            return False, "Account not created, Retry"
        self.accounts.append(account)
        self.__updateTotalBalance()
        for customer in Customer.allCustomer:
            if self.username == customer.username:
                customer.accounts = self.accounts
                customer.totalBalance = self.totalBalance
        return True, "Account Created"

