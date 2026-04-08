# Find the sum of three-digit number.
num = int(input("Enter a first digit :"))

digit1 = num % 10
digit2 = (num // 10) % 10
digit3 = num // 100

sum = digit1 + digit2 + digit3

print("Sum of digits =", sum) 