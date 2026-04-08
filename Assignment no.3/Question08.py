#Write a program to prompt user to enter userid and password. After verifying userid and password display a 4 digit random number and ask user to enter the same. If user enters the same number then show him success message otherwise failed. (Something like captcha)
import random
correct_userid = "admin"
correct_password = "1234"

userid = input("Enter User ID: ")
password = input("Enter Password: ")

if userid == correct_userid and password == correct_password:
    
    captcha = random.randint(1000, 9999)
    print("Captcha:", captcha)
    
    user_captcha = int(input("Enter the captcha: "))
    
    if user_captcha == captcha:
        print("Login Successful")
    else:
        print("Captcha incorrect Login Failed")

else:
    print("Invalid User ID or Password")
