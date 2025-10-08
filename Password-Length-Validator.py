#Password length checker
password = input("Enter your password:")
passwordlength = len(password)
if passwordlength >= 8:
     print("Password length is valid.")
else:
    print("Your password is too long or short. Please try again.")