import re
s1="i am learning python with rafi"
result=re.findall(r"[aeiouAEIOU]\w+",s1)
print(result)