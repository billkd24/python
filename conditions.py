age = int (input("Please enter your age:"))

if age >= 18:
    print ("Elgible to Drive")
else:
    print ("Not elgible to Drive")
    print (f"Please come back after {18-age} years.")
