import pandas as pd
import numpy as np

df = pd.read_csv('/Users/serenazhang/Desktop/Course materials/capstone/dataset/LGA_Everything/LGA/Sydney1.csv')
df['split'] = np.random.randn(df.shape[0], 1)

msk = np.random.rand(len(df)) <= 0.5

train = df[msk]
test = df[~msk]

train.to_csv('/Users/serenazhang/Desktop/Course materials/capstone/dataset/LGA_Everything/LGA/Sydney3.csv', index=False)
test.to_csv('/Users/serenazhang/Desktop/Course materials/capstone/dataset/LGA_Everything/LGA/2_2000.csv', index=False)