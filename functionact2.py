pin_number = 1234
withdrawalamount = 200
balance = 300

def cash_machine(pin_number, withdrawalamount, balance):
    if(pin_number == 1234 and withdrawalamount <= balance):
        print("\nHere is your cash\n")
        balance -= withdrawalamount
        print("Your new balance is: {}\n".format(balance))
    elif(pin_number != 1234):
        print("\nYou have entered the wrong pin\n")
    elif(pin_number == 1234 and withdrawalamount > balance):
        print("\nYou do not have enough in your account")
        print("Your balance is: {}\n".format(balance))
    else:
        print("\nError\n")

cash_machine(pin_number, withdrawalamount, balance)