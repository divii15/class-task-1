# 3. Create a class "BankAccount" with attributes account_number and balance. Add methods to deposit and withdraw money.

   **Input:**  
   Account Number: 12345  
   Initial Balance: 1000  
   Deposit: 500  
   Withdraw: 300  

   **Output:**  
   Account Number: 12345  
   Balance after deposit: 1500  
   Balance after withdrawal: 1200  



    class money:
    def __init__(self,account_number,initial_balance):
        self.account_number=account_number
        self.balance=initial_balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
account=money(12345,1000)
print(f"Account Number:{account.account_number}")
balance_deposit=account.deposit(500)
print(f"Balance after deposit:{balance_deposit}")
balance_withdrawal=account.withdraw(300)
print(f"Balance after withdrawal:{balance_withdrawal}")