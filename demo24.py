import re
input=input("Enter an input string:")
m=re.match('\d{5}\z',input)
if m:
    print("True")
else:
    print("False")