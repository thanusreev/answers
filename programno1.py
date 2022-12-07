import re
phone_regex="^[\+]?[)]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
phone_number=input("enter your contact number\n")
valid=re.search(phone_regex,phone_number)
if valid:
    print("contact number is valid ")
else:
    print("contact number is not valid")

