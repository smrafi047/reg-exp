import re
s1="i am learning python with Rafi"
result=re.findall(r"\w*",s1)
print(result)