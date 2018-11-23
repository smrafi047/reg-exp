import re
s1="rafi@gmail.com rafishaik@yahoo.com smrafi@co.in"
result=re.findall(r"@\w\w+",s1)
print(result)