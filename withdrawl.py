account_balance = input("Please enter your account balance: ")
withdrawl_ammount = input("Enter the amount you want to withdraw: ")

if int(account_balance) >=int(withdrawl_ammount):
    print("Withdrawl sucessful! Your new account balance is" , int(account_balance)-int(withdrawl_ammount))
else:
    print("Withdrawl unsucessful. Insufficient funds")
