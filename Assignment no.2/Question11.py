#Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.
amount = int(input("Enter amount: "))

notes_70 = amount // 70
amount = amount % 70

notes_30 = amount // 30
amount = amount % 30

notes_10 = amount // 10
amount = amount % 10

notes_5 = amount // 5
amount = amount % 5

notes_2 = amount // 2
amount = amount % 2

notes_1 = amount

print("50 notes =", notes_70)
print("20 notes =", notes_30)
print("10 notes =", notes_10)
print("5 notes =", notes_5)
print("2 notes =", notes_2)
print("1 notes =", notes_1)