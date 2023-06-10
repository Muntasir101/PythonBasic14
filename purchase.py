while True:
    try:
        purchase_amount = float(input("Enter the purchase amount (in TK): "))
        if purchase_amount < 0:
            raise ValueError("Purchase amount cannot be negative.")
        break
    except ValueError as e:
        print("Invalid input. Please enter a valid purchase amount.")

while True:
    try:
        age = int(input("Enter the customer's age: "))
        if age < 0:
            raise ValueError("Age cannot be negative.")
        break
    except ValueError as e:
        print("Invalid input. Please enter a valid age.")

while True:
    gender = input("Enter the customer's gender (male/female): ").lower()
    if gender not in ["male", "female"]:
        print("Invalid input. Please enter either 'male' or 'female'.")
    else:
        break

while True:
    payment_method = input("Enter the payment method (cash/card): ").lower()
    if payment_method not in ["cash", "card"]:
        print("Invalid input. Please enter either 'cash' or 'card'.")
    else:
        break

if purchase_amount < 1000 or age >= 50:
    print("Sorry, you are not eligible for any free item or discount.")
    payable_amount = purchase_amount
else:
    if gender == "male":
        free_item = "cake"
    elif gender == "female":
        free_item = "chocolate"

    if payment_method == "cash":
        discount = purchase_amount * 0.1
    elif payment_method == "card":
        discount = purchase_amount * 0.2

    payable_amount = purchase_amount - discount

    if gender in ["male", "female"]:
        print("Congratulations! You get a free", free_item)

    print("Payable Amount:", payable_amount, "TK")
