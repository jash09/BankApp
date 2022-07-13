from account import Account
from bank import Bank
from customer import Customer


if __name__ == "__main__":
    Bank.createNewBank("Bank of Baroda", "BoB")
    Bank.createNewBank("State Bank of India", "SBI")
    Bank.createNewBank("international Bank", "IB")
    Bank.createNewBank("Punjab National Bank", "PBI")

    Jash = Customer.createNewCustomer("Jash", "Shah", "jashhshahh")
    Rock = Customer.createNewCustomer("Rock", "Smith", "rsmith")

    Jash.createNewAccount("SBI")
    Jash.createNewAccount("BoB")
    Jash.createNewAccount("IB")
    Rock.createNewAccount("IB")

    Jash.displayBalance("BoB")
    Rock.displayBalance("IB")
    print("\n")

    Jash.displayTotalBalance()
    Rock.displayTotalBalance()
    print("\n")

    Jash.selfTransfer("BoB", 800, "IB")
    Jash.displayTotalBalance()
    print("\n")
    
    Jash.deposit(100, "IB")
    Rock.deposit(2500, "IB")
    print("\n")

    Jash.withdraw(3100, "IB")
    Jash.withdraw(2900, "IB")
    print("\n")



    Jash.displayBalance("BoB")
    Jash.displayBalance("SBI")
    Jash.displayBalance('IB')
    Jash.transferAmount("rsmith", "IB", "IB", 10)