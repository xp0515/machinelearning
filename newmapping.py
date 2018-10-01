import shapefile
import csv
from shapely.geometry import Point, shape

shp = shapefile.Reader(r'/Users/serenazhang/Desktop/Course materials/capstone/1270055003_lga_2016_aust_shape/LGA_2016_AUST.shp')
all_shapes = shp.shapes()
all_records = shp.records()

f = open(r'/Users/serenazhang/Desktop/Course materials/capstone/xp_tweets.csv')
reader = csv.DictReader(f)
new_list = list()

for row in reader:
    lat = row['lat']
    lng = row['lng']
    lat = float(lat)
    lng = float(lng)

    for i in range(130):
        boundary = all_shapes[i]
        if Point(lng, lat).within(shape(boundary)):
            row['LGA_CODE'] = all_records[i][0]
            print(row)
            new_list.append(row)

headers = ['id', 'created_at', 'text', 'from_user_id',  'from_user_followercount', 'from_user_friendcount', 'lang', 'lat', 'lng', 'LGA_CODE']
with open('/Users/serenazhang/Desktop/Course materials/capstone/dataset/xp_tweets_LGA.csv', 'w', newline='') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(new_list)
