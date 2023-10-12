#Set B

#1

import pandas as pd
from matplotlib.pyplot import*
df=pd.read_csv("Iris.csv")
print(df)
print(df.sample(20))
print("max of sepal length:",max(df["SepalLengthCm"]))
print("max of petal length:",max(df["PetalWidthCm"]))
print("max of sepal length:",min(df["SepalLengthCm"]))
print("min of petal lenght:",min(df["PetalWidthCm"]))

#2
print("No. of record of distinct value of class attribute ia:\n")
print(df["Species"].value_counts())

#3
Means=df["SepalLengthCm"].mean().round(2)
print("mean of class attribute sepalLengthCm is:",Means)

Means=df["PetalLengthCm"].mean().round(2)
print("mean of class attribute petalLengthCm is:",Means)

Meds=df["SepalLengthCm"].mean().round(2)
print("median of class attribute sepalLengthCm is:",Meds)

Meds=df["PetalLengthCm"].mean().round(2)
print("median of class attribute petalLengthCm is:",Meds)
