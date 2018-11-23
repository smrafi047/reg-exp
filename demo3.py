import re
st="Rafi is here"
result=re.match(r"Rafi",st)
print(result.group(0))
