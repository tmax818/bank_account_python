from bank_account import BankAccount

# Create 2 accounts

acct1 = BankAccount(.1, 1000)
acct2 = BankAccount(.2, 2000)
#
# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in
# one line of code (i.e. chaining)

acct1.deposit(1000).deposit(1000).deposit(1000).withdraw(2000).yield_interest().display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in
# one line of code (i.e. chaining)

acct2.deposit(10000).deposit(10000).withdraw(2000).withdraw(2000).withdraw(2000).withdraw(2000).yield_interest().display_account_info()


