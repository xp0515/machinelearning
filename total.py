import csv
from datetime import datetime

new_list = list()
i1 = i2 = i3 = i4 = i5 = i6 = i7 = i8 =  1
j1 = j2 = j3 = j4 = j5 = j6 = j7 = j8 =  1
m1 = m2 = m3 = m4 = m5 = m6 = m7 = m8 =  0
n1 = n2 = n3 = n4 = n5 = n6 = n7 = n8 =  0
with open("/Users/serenazhang/Desktop/Course materials/capstone/dataset/LGA_Everything/10750.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:

        a = row['created_at']
        a = datetime.strptime(a, '%d/%m/%y')

        if datetime(2018, 1, 11) <= a <= datetime(2018, 1, 17):
            if int(row['score']) > 0:
                row['total_positive'] = i1
                i1 = i1 + 1
                row['timing_positive'] = int(row['time']) + m1
                m1 = row['timing_positive']
            elif int(row['score']) < 0:
                row['total_negative'] = j1
                j1 = j1 + 1
                row['timing_negative'] = int(row['time']) + n1
                n1 = row['timing_negative']

with open("/Users/serenazhang/Desktop/Course materials/capstone/dataset/LGA_Everything/10750.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:

        a = row['created_at']
        a = datetime.strptime(a, '%d/%m/%y')

        if datetime(2018, 1, 18) <= a <= datetime(2018, 1, 24):
            if int(row['score']) > 0:
                row['total_positive'] = i2
                i2 = i2 + 1
                row['timing_positive'] = int(row['time']) + m2
                m2 = row['timing_positive']
            elif int(row['score']) < 0:
                row['total_negative'] = j2
                j2 = j2 + 1
                row['timing_negative'] = int(row['time']) + n2
                n2 = row['timing_negative']

with open("/Users/serenazhang/Desktop/Course materials/capstone/dataset/LGA_Everything/10750.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:

        a = row['created_at']
        a = datetime.strptime(a, '%d/%m/%y')

        if datetime(2018, 1, 25) <= a <= datetime(2018, 1, 31):
            if int(row['score']) > 0:
                row['total_positive'] = i3
                i3 = i3 + 1
                row['timing_positive'] = int(row['time']) + m3
                m3 = row['timing_positive']
            elif int(row['score']) < 0:
                row['total_negative'] = j3
                j3 = j3 + 1
                row['timing_negative'] = int(row['time']) + n3
                n3 = row['timing_negative']

with open("/Users/serenazhang/Desktop/Course materials/capstone/dataset/LGA_Everything/10750.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:

        a = row['created_at']
        a = datetime.strptime(a, '%d/%m/%y')

        if datetime(2018, 2, 1) <= a <= datetime(2018, 2, 7):
            if int(row['score']) > 0:
                row['total_positive'] = i4
                i4 = i4 + 1
                row['timing_positive'] = int(row['time']) + m4
                m4 = row['timing_positive']
            elif int(row['score']) < 0:
                row['total_negative'] = j4
                j4 = j4 + 1
                row['timing_negative'] = int(row['time']) + n4
                n4 = row['timing_negative']

with open("/Users/serenazhang/Desktop/Course materials/capstone/dataset/LGA_Everything/10750.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:

        a = row['created_at']
        a = datetime.strptime(a, '%d/%m/%y')

        if datetime(2018, 2, 8) <= a <= datetime(2018, 2, 14):
            if int(row['score']) > 0:
                row['total_positive'] = i5
                i5 = i5 + 1
                row['timing_positive'] = int(row['time']) + m5
                m5 = row['timing_positive']
            elif int(row['score']) < 0:
                row['total_negative'] = j5
                j5 = j5 + 1
                row['timing_negative'] = int(row['time']) + n5
                n5 = row['timing_negative']

with open("/Users/serenazhang/Desktop/Course materials/capstone/dataset/LGA_Everything/10750.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:

        a = row['created_at']
        a = datetime.strptime(a, '%d/%m/%y')

        if datetime(2018, 2, 15) <= a <= datetime(2018, 2, 21):
            if int(row['score']) > 0:
                row['total_positive'] = i6
                i6 = i6 + 1
                row['timing_positive'] = int(row['time']) + m6
                m6 = row['timing_positive']
            elif int(row['score']) < 0:
                row['total_negative'] = j6
                j6 = j6 + 1
                row['timing_negative'] = int(row['time']) + n6
                n6 = row['timing_negative']

with open("/Users/serenazhang/Desktop/Course materials/capstone/dataset/LGA_Everything/10750.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:

        a = row['created_at']
        a = datetime.strptime(a, '%d/%m/%y')

        if datetime(2018, 2, 22) <= a <= datetime(2018, 2, 28):
            if int(row['score']) > 0:
                row['total_positive'] = i7
                i7 = i7 + 1
                row['timing_positive'] = int(row['time']) + m7
                m7 = row['timing_positive']
            elif int(row['score']) < 0:
                row['total_negative'] = j7
                j7 = j7 + 1
                row['timing_negative'] = int(row['time']) + n7
                n7 = row['timing_negative']

with open("/Users/serenazhang/Desktop/Course materials/capstone/dataset/LGA_Everything/10750.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:

        a = row['created_at']
        a = datetime.strptime(a, '%d/%m/%y')

        if datetime(2018, 3, 1) <= a <= datetime(2018, 3, 6):
            if int(row['score']) > 0:
                row['total_positive'] = i8
                i8 = i8 + 1
                row['timing_positive'] = int(row['time']) + m8
                m8 = row['timing_positive']
            elif int(row['score']) < 0:
                row['total_negative'] = j8
                j8 = j8 + 1
                row['timing_negative'] = int(row['time']) + n8
                n8 = row['timing_negative']


with open("/Users/serenazhang/Desktop/Course materials/capstone/dataset/LGA_Everything/10750.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:

        a = row['created_at']
        a = datetime.strptime(a, '%d/%m/%y')

        if datetime(2018, 1, 11) <= a <= datetime(2018, 1, 17):
            row['total_positive'] = i1 - 1
            row['total_negative'] = j1 - 1
            row['timing_positive'] = m1/(i1 - 1)
            row['timing_negative'] = n1/(j1 - 1)
            print(row)
            new_list.append(row)

with open("/Users/serenazhang/Desktop/Course materials/capstone/dataset/LGA_Everything/10750.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:

        a = row['created_at']
        a = datetime.strptime(a, '%d/%m/%y')

        if datetime(2018, 1, 18) <= a <= datetime(2018, 1, 24):
            row['total_positive'] = i2 - 1
            row['total_negative'] = j2 - 1
            row['timing_positive'] = m2/(i2 - 1)
            row['timing_negative'] = n2/(j2 - 1)
            print(row)
            new_list.append(row)

with open("/Users/serenazhang/Desktop/Course materials/capstone/dataset/LGA_Everything/10750.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:

        a = row['created_at']
        a = datetime.strptime(a, '%d/%m/%y')

        if datetime(2018, 1, 25) <= a <= datetime(2018, 1, 31):
            row['total_positive'] = i3 - 1
            row['total_negative'] = j3 - 1
            row['timing_positive'] = m3/(i3 - 1)
            row['timing_negative'] = n3/(j3 - 1)
            print(row)
            new_list.append(row)

with open("/Users/serenazhang/Desktop/Course materials/capstone/dataset/LGA_Everything/10750.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:

        a = row['created_at']
        a = datetime.strptime(a, '%d/%m/%y')

        if datetime(2018, 2, 1) <= a <= datetime(2018, 2, 7):
            row['total_positive'] = i4 - 1
            row['total_negative'] = j4 - 1
            row['timing_positive'] = m4/(i4 - 1)
            row['timing_negative'] = n4/(j4 - 1)
            print(row)
            new_list.append(row)

with open("/Users/serenazhang/Desktop/Course materials/capstone/dataset/LGA_Everything/10750.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:

        a = row['created_at']
        a = datetime.strptime(a, '%d/%m/%y')

        if datetime(2018, 2, 8) <= a <= datetime(2018, 2, 14):
            row['total_positive'] = i5 - 1
            row['total_negative'] = j5 - 1
            row['timing_positive'] = m5/(i5 - 1)
            row['timing_negative'] = n5/(j5 - 1)
            print(row)
            new_list.append(row)

with open("/Users/serenazhang/Desktop/Course materials/capstone/dataset/LGA_Everything/10750.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:

        a = row['created_at']
        a = datetime.strptime(a, '%d/%m/%y')

        if datetime(2018, 2, 15) <= a <= datetime(2018, 2, 21):
            row['total_positive'] = i6 - 1
            row['total_negative'] = j6 - 1
            row['timing_positive'] = m6/(i6 - 1)
            row['timing_negative'] = n6/(j6 - 1)
            print(row)
            new_list.append(row)

with open("/Users/serenazhang/Desktop/Course materials/capstone/dataset/LGA_Everything/10750.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:

        a = row['created_at']
        a = datetime.strptime(a, '%d/%m/%y')

        if datetime(2018, 2, 22) <= a <= datetime(2018, 2, 28):
            row['total_positive'] = i7 - 1
            row['total_negative'] = j7 - 1
            row['timing_positive'] = m7/(i7 - 1)
            row['timing_negative'] = n7/(j7 - 1)
            print(row)
            new_list.append(row)

with open("/Users/serenazhang/Desktop/Course materials/capstone/dataset/LGA_Everything/10750.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:

        a = row['created_at']
        a = datetime.strptime(a, '%d/%m/%y')

        if datetime(2018, 3, 1) <= a <= datetime(2018, 3, 6):
            row['total_positive'] = i8 - 1
            row['total_negative'] = j8 - 1
            row['timing_positive'] = m8/(i8 - 1)
            row['timing_negative'] = n8/(j8 - 1)
            print(row)
            new_list.append(row)

headers = ['id','created_at','hour','minute','second','text','from_user_id','from_user_followercount','from_user_friendcount','lang','lat','lng','LGA_CODE',
           'Median_age_persons','Median_mortgage_repay_monthly','Median_tot_prsnl_inc_weekly','Median_rent_weekly','Median_tot_fam_inc_weekly',
           'Average_num_psns_per_bedroom','Median_tot_hhd_inc_weekly','Average_household_size','Counted_Census_Night_home_P','Lang_spoken_home_Eng_only_P',
           'Australian_citizen_P','Marital_Prop','anger','anticipation','disgust','fear','joy','sadness','surprise','trust','negative','positive','score','Crime_Rate',
           'Y', 'day', 'time','LGA','y1','total_positive','total_negative','timing_positive','timing_negative']
with open('/Users/serenazhang/Desktop/Course materials/capstone/dataset/LGA_Everything/10750new.csv', 'w', newline='') as f:
    f_csv = csv.DictWriter(f, headers)
    f_csv.writeheader()
    f_csv.writerows(new_list)