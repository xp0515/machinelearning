import pandas as pd

a = pd.read_csv("/Users/serenazhang/Desktop/Course materials/capstone/dataset/y6.csv")
b = pd.read_csv("/Users/serenazhang/Desktop/Course materials/capstone/dataset/Book2.csv")

merged = a.merge(b, on='LGA_CODE')
merged.to_csv("/Users/serenazhang/Desktop/Course materials/capstone/dataset/y50.csv", index=False)