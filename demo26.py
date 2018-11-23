import re
input="contact me by mahammadrafi@gmail.com or at the office."
m=re.search('[^@]+#[^@]+\.[^@]+',input)
if m:
    print("string found.")
else:print("Nothing found.")