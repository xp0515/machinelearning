import csv
import datetime

f = open("/Users/serenazhang/Desktop/Course materials/capstone/dataset/G1_000.csv")
reader = csv.DictReader(f)
new_list = list()

for row in reader:

    a = row['created_at']
    day, month, year = (int(x) for x in a.split('/'))
    day = datetime.date(year, month, day)
    print(day.weekday())
    row['day'] = day.weekday()

    b = row['hour']
    if 0 <= int(b) < 6:
        row['time'] = 1
    elif 6 <= int(b) < 12:
        row['time'] = 2
    elif 12 <= int(b) < 18:
        row['time'] = 3
    elif 18 <= int(b) <= 23:
        row['time'] = 4
    new_list.append(row)

headers = ['id','created_at','hour','minute','second','text','from_user_id','from_user_followercount','from_user_friendcount',
           'lang','lat','lng','LGA_CODE','Median_age_persons','Median_mortgage_repay_monthly','Median_tot_prsnl_inc_weekly',
           'Median_rent_weekly','Median_tot_fam_inc_weekly','Average_num_psns_per_bedroom','Median_tot_hhd_inc_weekly',
           'Average_household_size','Counted_Census_Night_home_P','Lang_spoken_home_Eng_only_P','Australian_citizen_P',
           'Marital_Prop','anger','anticipation','disgust','fear','joy','sadness','surprise','trust','negative','positive',
           'Crime_Rate','Y', 'day', 'time']
with open('/Users/serenazhang/Desktop/Course materials/capstone/dataset/everything.csv', 'w', newline='') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(new_list)
