from replit import clear
from LOGO import LOGO
from email_validation import check
from sheety_api import update_sheets

# Clear Screen
clear()
# Print Flight Club Logo and welcome prompt
print(LOGO)
print("Hello and welcome to Flight Club new user registration page\n")

# Collecting new user's first name , last name and email address
first_name = input("Please Enter your first Name\n").capitalize()
last_name = input("Please Enter your last Name\n").capitalize()

# Get email and check email validity
email_confirmed = False
while not email_confirmed:
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
        if valid_email2 == False:
            print("The email address you entered is not valid")

    if email1 == email2:
        email_confirmed = True
    else:
        print("Your email addresses did not match")



if first_name and last_name:
    # ready for sheets update
    update_sheets(first_name, last_name, email1)
else:
    print("Sorry you did not enter your name properly, please refresh and run again")