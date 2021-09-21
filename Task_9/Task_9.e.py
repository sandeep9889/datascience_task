print("name: sandeep chouhan")
print("scholar no: 30203")
import re
num = "07987549836" 
print("Initial number:",num)
pattern = r"9"
num = re.sub(pattern, "0",num) 
print("Number after substituion:",num)