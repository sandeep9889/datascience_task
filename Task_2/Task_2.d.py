print("name: sandeep chouhan")
print("scholar no: 30203")
row_1=['Facebook',0.0,'USD',2974676,3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5=['Pandora - Music & Radio',0.0,'USD',1126879,4.0]
fb_rating_data=[row_1[0],row_1[3],row_1[4]]
insta_rating_data=[row_2[0],row_2[3],row_2[4]]
pandora_rating_data=[row_5[0],row_5[3],row_5[4]]
avg_rating=(fb_rating_data[2]+insta_rating_data[2]+pandora_rating_data[2])/3
print(avg_rating)
