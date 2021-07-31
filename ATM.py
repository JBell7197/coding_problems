#draws user inputs
account_balance = float(input("How much money do you have in your account? "))
withdrawal = float(input("How much money would you like to withdraw? "))

#adds bank charge and multiple of 5
correct_withdrawal = withdrawal % 5
whole_withdrawal = (withdrawal + 0.50)

#calculating remains
remaining_balance = account_balance - whole_withdrawal

#conditions
if remaining_balance >= 0 and correct_withdrawal == 0:
    remaining_balance = "{:.2f}".format(remaining_balance)
    print("Your remaining balance is: ", remaining_balance)
elif remaining_balance < 0:
    account_balance = "{:.2f}".format(account_balance)
    print("You don't have enough funds. Your current bank balance is: ", account_balance)
elif correct_withdrawal != 0:
    print("It has to be a multiple of 5")