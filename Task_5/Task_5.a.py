print("name: sandeep chouhan")
print("scholar no: 30203")
from csv import reader
file=open("artists.csv","r",encoding="utf8")
read_file=reader(file)
artists=list(read_file)
artists=artists[1:]

num_rows=len(artists)

print("Number of rows in MoMA dataset:",num_rows)