print("name: sandeep chouhan")
print("scholar no: 30203")
from csv import reader
file=open("AppleStore.csv","r",encoding="utf8")
opened_file=reader(file)
apps_data=list(opened_file)
apps_data=apps_data[1:]

rating_sum=0
for rating in apps_data:
    rating_sum += float(rating[8])
avg_rating = rating_sum/len(apps_data)
print(avg_rating)