# Hard-coded version of the ATM cash withdrawal program

# Initialize variables for the amount of cash available in the ATM and the notes available
cash_available = 40000
rs2000_notes = 10
rs500_notes = 25
rs100_notes = 75

# Prompt the user for their debit card number and ATM pin
debit_card_number = input("Enter your debit card number: ")
atm_pin = input("Enter your ATM pin: ")

# Validate the debit card number and ATM pin using hard-coded values
if debit_card_number != "123456789012":
    print("Invalid debit card number.")
elif atm_pin != "1234":
    print("Invalid ATM pin.")
else:
    # Prompt the user for the amount they want to withdraw
    withdrawal_amount = int(input("Enter the amount you want to withdraw: "))

    # Check if the withdrawal amount is available in the ATM
    if withdrawal_amount > cash_available:
        print("Insufficient cash available in the ATM.")
    elif withdrawal_amount > 10000:
        print("You can't withdraw more than Rs.10000 in a single transaction.")
    else:
        # Calculate the number of each type of note needed to fulfill the withdrawal request
        rs2000_needed = withdrawal_amount // 2000
        rs500_needed = (withdrawal_amount % 2000) // 500
        rs100_needed = ((withdrawal_amount % 2000) % 500) // 100

        # Check if there are enough notes of each type available in the ATM
        if rs2000_needed > rs2000_notes:
            print("Insufficient Rs.")
