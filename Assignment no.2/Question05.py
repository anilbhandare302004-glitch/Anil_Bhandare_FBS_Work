# WAP to calculate selling price of book based on cost price and discount.
cost_price = float(input("Enter a cost price :" ))
discount_percentage = float(input("Ente a discount percentage :"))

discount_amount = (discount_percentage / 100) * cost_price
selling_price = cost_price - discount_amount

print("Discount Amount is =", discount_amount)
print("Selling Price is =", selling_price)