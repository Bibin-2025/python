
class Account:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

  
    def __add__(self, other):
        if isinstance(other, Account):
            return self._balance + other._balance
        return NotImplemented

   
    def display(self):
        print(f"Account Holder: {self._name}")
        print(f"Balance: ₹{self._balance:.2f}")


class SavingsAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.05  # 5% interest



class CurrentAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.02  # 2% interest



savings_acc = SavingsAccount("Ravi", 10000)
current_acc = CurrentAccount("Anjali", 15000)

print("=== Savings Account ===")
savings_acc.display()
print(f"Interest (5%): ₹{savings_acc.calculate_interest():.2f}")


print("\n=== Current Account ===")
current_acc.display()
print(f"Interest (2%): ₹{current_acc.calculate_interest():.2f}")

total_balance = savings_acc + current_acc
print("\n=== Total Balance (Ravi + Anjali) ===")
print(f"Combined Balance: ₹{total_balance:.2f}")
