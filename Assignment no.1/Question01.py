#Write a program to calculate the percentage of student based on marks of any 5 subjects.

sub1 = int(input("Enter marks of sub1 :"))
sub2 = int(input("Enter marks of sub2 :"))
sub3 = int(input("Enter marks of sub3 :"))
sub4 = int(input("Enter marks of sub4 :"))
sub5 = int(input("Enter marks of sub5 :"))

sum = sub1 + sub2 + sub3 + sub4 + sub5 

calculatePercentage = ( sum / 500)*100
print('Total sum =',sum)
print('percentage of : .',calculatePercentage)
