import re
user_name=input("Name please:")
result=re.match("^[A-Za-z]*$",user_name)
if result==None:
    print("invalid name")
else:
    print("welcome mr/miss:",user_name)