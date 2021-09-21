print("name: sandeep chouhan")
print("scholar no: 30203")
from csv import reader
file=open("AppleStore.csv","r",encoding="utf8")
opened_file=reader(file)
apps_data=list(opened_file)

print(len(apps_data),"\n")
print(apps_data[0],"\n")
print(apps_data[1:3])