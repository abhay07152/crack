from random import *
user_pass=input("enter  your password\n")
password=["1","2","3","4","5","6","7","8","9","0"]
guess=""
while(guess!=user_pass):
    # guess=""
    for letter in range(len(user_pass)):
        guess_letter=password[randint(0,9)]
        guess=str(guess_letter)+str(guess)
        print(guess)
print("your password is ",guess)
