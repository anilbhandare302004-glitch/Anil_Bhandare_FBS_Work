#Write a program to input any alphabet and check whether it is vowel or consonant.
alphabate = input("Enter an alphabet: ")

if alphabate.lower() in ('a', 'e', 'i', 'o', 'u'):
    print("It is a Vowel letter.")
else:
    print("It is a Consonant letter.")