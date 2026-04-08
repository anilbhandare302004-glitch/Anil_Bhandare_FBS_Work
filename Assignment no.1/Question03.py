#Write a program to enter P, T, R and calculate Compound Interest.

P = int(input('Enet a Peinciple :'))
T = int(input('Enter a Time :'))
R = int(input('Enter a Rate :'))

compoundIntrest = P *(1 + R / 100) **T

CI = compoundIntrest - P

print('Calculate Total Amount of Compound Intrest is :',compoundIntrest)
print('The Compound Intrest is :',CI)