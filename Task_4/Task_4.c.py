print("name: sandeep chouhan")
print("scholar no: 30203")
from csv import reader
file=open("AppleStore.csv","r",encoding="utf8")
opened_file=reader(file)
apps_data=list(opened_file)
apps_data=apps_data[1:]

all_ratings=list()
for rating in apps_data:
    all_ratings.append(float(rating[8]))
avg_rating = sum(all_ratings)/len(apps_data)
print(avg_rating)