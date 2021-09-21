print("name: sandeep chouhan")
print("scholar no: 30203")
from csv import reader
file=open("AppleStore.csv","r",encoding="utf8")
opened_file=reader(file)
apps_data=list(opened_file)
apps_data=apps_data[1:]

for row in apps_data:
    print(row)