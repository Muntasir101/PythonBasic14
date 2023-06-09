"""
Discount Calculation:
Up to purchase 10000 = Discount 10%
purchase 10000 to 20000 = Discount 15%
purchase 20000 to 50000 = Discount 20%
more than 50000 = Discount 30%
"""

purchase_amount = float(input("Purchase amount: "))
discount = 0

if purchase_amount <= 10000:
    discount = purchase_amount * 0.1
elif purchase_amount <= 20000:
    discount = purchase_amount * 0.15
elif purchase_amount <= 50000:
    discount = purchase_amount * 0.3
else:
    discount = purchase_amount * 0.5

amount_payable = purchase_amount - discount
print("You received Discount: ", discount)
print("You have to pay:", amount_payable)
