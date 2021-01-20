from replit import clear
from LOGO import LOGO
from email_validation import check


# Clear Screen
clear()
# Print Flight Club Logo and welcome prompt
print(LOGO)
print("Hello and welcome to Flight Club new user registration page\n")

# Collecting new user's first name , last name and email address
first_name = input("Please Enter your first Name\n").capitalize()
last_name = input("Please Enter your last Name\n").capitalize()

# Get email and check email validity
valid_email1 = False
while not valid_email1:
    email1 = input("Please enter your email address\n")
    valid_email1 = check(email1)
    if valid_email1 == False:
        print("The email address you entered is not valid")

valid_email2 = False
while not valid_email2:
    email2 = input("Please comfirm your email address\n")
    valid_email2 = check(email2)
    if valid_email1 == False:
        print("The email address you entered is not valid")




