#Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

A = int(input("enter 1st person ticket amount : "))
B = int(input("enter 2st person ticket amount : "))
C = int(input("enter 3st person ticket amount : "))
D = int(input("enter 4st person ticket amount : "))
E = int(input("enter 5st person ticket amount : "))

sum = 8 + 11 + 75 + 66 + 55
print("Total amount of ticket is :",sum)
if( 8 <= 12 ):
    print("30% discount for below 12 age ")
else:
    print("no discount")
if(75>=59):
     print("50% discount for senior citizen above age 59")
else:
    print("no discont")
if(25==25):
    print("need to pay full amount of tickets.")
            