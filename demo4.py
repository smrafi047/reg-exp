import re
st="This is Rafi"
result=re.search(r"Rafi",st)
print(result)
print(result.group(0))