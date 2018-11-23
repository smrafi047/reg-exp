import re
s1="Hi 007 this is 001 from python"
result=re.findall(r"\d",s1)
print(result)