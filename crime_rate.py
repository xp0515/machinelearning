import csv

a = open('/Users/serenazhang/Desktop/Course materials/capstone/dataset/LGA_Everything/18500new.csv')
reader_a = csv.DictReader(a)
b = open('/Users/serenazhang/Desktop/Course materials/capstone/LGA_crime/New/Woollahra.csv')
reader_b = csv.DictReader(b)
new_list = list()

for row_a in reader_a:
    date = row_a['created_at'].split('/')
    month = date[1]
    index = row_a['day'] + row_a['time']

    for row_b in reader_b:
        if month == row_b['Month']:
            row_a['y'] = row_b[index]
            new_list.append(row_a)
    b.seek(0)

headers = ['id','created_at','hour','minute','second','text','from_user_id','from_user_followercount','from_user_friendcount','lang','lat','lng','LGA_CODE',
           'Median_age_persons','Median_mortgage_repay_monthly','Median_tot_prsnl_inc_weekly','Median_rent_weekly','Median_tot_fam_inc_weekly',
           'Average_num_psns_per_bedroom','Median_tot_hhd_inc_weekly','Average_household_size','Counted_Census_Night_home_P','Lang_spoken_home_Eng_only_P',
           'Australian_citizen_P','Marital_Prop','anger','anticipation','disgust','fear','joy','sadness','surprise','trust','negative','positive','score','Crime_Rate',
           'Y', 'day', 'time','LGA','y1','total_positive','total_negative','timing_positive','timing_negative', 'y']
with open('/Users/serenazhang/Desktop/Course materials/capstone/dataset/LGA_Everything/LGA/18500.csv', 'w', newline='') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(new_list)



