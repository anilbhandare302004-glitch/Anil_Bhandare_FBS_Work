#Input 5 subject marks from user and display grade(eg.First class,Second class ..)
sub1 = int(input("Enter marks for sub1 :"))
sub2 = int(input("Enter marks for sub2 :"))
sub3 = int(input("Enter marks for sub3 :"))
sub4 = int(input("Enter marks for sub4 :"))
sub5 = int(input("Enter marks for sub5 :"))

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = total / 5

print("Percentage =", percentage)

if percentage >= 60:
    print("First Class.")
elif percentage >= 50:
    print("Second Class.")
elif percentage >= 40:
    print("Pass Class.")
else:
    print("Fail")