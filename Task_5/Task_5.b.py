print("name: sandeep chouhan")
print("scholar no: 30203")
from csv import reader
file=open("artists.csv","r",encoding="utf8")
read_file=reader(file)
artists=list(read_file)
artists=artists[1:]

#Cleaning Nationality Column
nationality=list()
for nationality in artists[2]:
    nationality.replace("(","")
    nationality.replace(")","")

#Cleaning Gender Column
gender=list()
for gender in artists[3]:
    gender.replace("(","")
    gender.replace(")","")
print("Data Cleaned Successfully!!")