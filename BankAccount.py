class BankAccount:

  def __init__(self, balance):

    balance = int(input("How much is in your Bank Account? "))
    self.balance = balance
    if self.balance < 0:
      return False
    interest = .02
    self.interest = interest


  def deposit(self, deposit_amount):
    deposit_amount = int(input("How much do you want to deposit? "))
    if deposit_amount < 0:
      return False
    else:
      self.balance += deposit_amount
      return(self.balance)


  def withdraw(self, withdraw_amount):
      withdraw_amount = int(input("How much would you like to withdraw? "))
      if withdraw_amount < 0:
        return False
      else:
          self.balance -= withdraw_amount
          return (self.balance)
  def accumulate_interest(self, interest_rate):
         self.balance -= (self.balance * interest_rate)
         return (self.balance)


...
class ChildrensAccount(BankAccount):
    pass
    # balance = (input("How much is in your childs Bank Account?"))
    def accumulate_interest(self, interest_rate):
        self.balance -= (self.balance * interest_rate)
        self.balance += 10
        return (self.balance)


class OverdraftAccount(BankAccount):
    pass
    def withdraw(self, withdraw_amount):
        withdraw_amount = int(input("How much would you like to withdraw? "))
        if withdraw_amount < 0:
            withdraw_amount = False
            return self.balance
        if (self.balance - withdraw_amount) < 0:
            withdraw_amount = False
            self.balance -= 40
            return self.balance
        else:
            self.balance -= withdraw_amount
            return self.balance
    # if self.balance < 0:
    #     def accumulate_interest(self, interest_rate):
    #         return False





basic_account = BankAccount(0)
basic_account.deposit(0)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(0)
print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest(.02)
print("Basic account has ${} after interest.".format(basic_account.balance))
print()



childs_account = ChildrensAccount(0)
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest(.02)
print("Child's account has ${}".format(childs_account.balance))
print()



overdraft_account = OverdraftAccount(0)
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest(0)
print("Overdraft account has ${}".format(overdraft_account.balance))
