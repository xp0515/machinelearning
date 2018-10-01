import pandas as pd

a = pd.read_csv('/Users/serenazhang/Desktop/Course materials/capstone/dataset/xp_tweets_LGA.csv')
b = pd.read_csv('/Users/serenazhang/Desktop/Course materials/capstone/xp_Census1.csv')
merged = a.merge(b, on = 'LGA_CODE')
merged.to_csv('/Users/serenazhang/Desktop/Course materials/capstone/dataset/tweets_census.csv', index = False)




