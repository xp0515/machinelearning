import csv
from time import sleep
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

geolocator = Nominatim(scheme='http', timeout=None)

with open('/Users/serenazhang/Desktop/Course materials/capstone/Book4.csv') as f:
    new_list = list()
    reader = csv.DictReader(f)
    for row in reader:
        lat = row['lat']
        lng = row['lng']

        coordinate = [lat, lng]
        val = ", ".join(coordinate)


        def do_geocode(val):
            try:
                return geolocator.reverse(val)
            except GeocoderTimedOut:
                return do_geocode(val)

        location = geolocator.reverse(val)
        row['LGA'] = location.raw['address']['county']
        print(row)
        new_list.append(row)
        sleep(1)


headers = ['id', 'created_at', 'text', 'from_user_id',  'from_user_followercount', 'from_user_friendcount', 'lang', 'lat', 'lng', 'LGA']
with open('/Users/serenazhang/Desktop/Course materials/capstone/xp_tweets_LGA13.csv', 'w', newline='') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(new_list)
