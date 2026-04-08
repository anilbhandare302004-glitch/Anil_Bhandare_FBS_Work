#Write a program to enter P, T, R and calculate simple Interest.

p = int(input('Enter principle :'))
T = int(input('Enter Time :'))
R = int(input('Enter Rate :'))

SimpleIntrest = (p * T * R) / 100

print('The Simple Intrest is :',SimpleIntrest)
