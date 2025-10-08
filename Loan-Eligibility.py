#Check if eligible for loan

credscore = int(input("Enter credit score:"))
anualinc = int(input("Enter annual income:"))
yearsjob = int(input("Enter current years at job:"))
    
#Check if enough
if credscore >= 700 and anualinc >= 30000 and yearsjob >= 2:
    print("Result: Loan aprroved.")
else:
    print("Result: Loan Denied.")

