print("name: sandeep chouhan")
print("scholar no: 30203")
row_1=['Facebook',0.0,'USD',2974676,3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5=['Pandora - Music & Radio',0.0,'USD',1126879,4.0]
app_data_set=[row_1,row_2,row_3,row_4,row_5]
avg_rating=(app_data_set[0][-1]+app_data_set[1][-1]+app_data_set[2][-1]+app_data_set[3][-1]+app_data_set[4][-1])/5
print(avg_rating)