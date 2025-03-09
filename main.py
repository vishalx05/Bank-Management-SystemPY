class BankAccount:
    def __init__(self,account_number,account_holder,balance=0):
        self.account_number=account_number
        self.account_holder=account_holder
        self.balance=balance


    def deposit(self,amount):
        if amount>=0:
            self.balance+=amount
            print(f"Deposited ${amount} successfully!")

        else:
            print("Invalid deposit")

    def withdraw(self,amount):
        if 0<amount<=self.balance:
            self.balance-=amount
            print(f"Withdrew ${amount} successfully!")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        print("Account Balance :"+ self.balance)

    def display_detail(self):
        print("="*30)
        print("Account Number ",self.account_number)
        print("Account Holder",self.account_holder)
        print("Balance Available ",self.balance)
        print("="*30)


obj=BankAccount(6744267423,"vikas",62474)
obj.deposit(2000)
obj.display_detail()
