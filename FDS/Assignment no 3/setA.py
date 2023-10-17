#SetA

import pandas as pd
from matplotlib.pyplot import*
df=pd.read_csv('data.csv')
print(df)

#1
print(df.describe())
print(df.shape)
print("display first 3 rows from dataset:",df.head(3))

#2
print(df.isnull())
print("Missing value replace with 0:",df.fillna(0,inplace=True))
print(df)

print("\n drop rows having value 0:",df.dropna())
Mean=df['Age'].mean()
print(Mean)
df["Age"].fillna(Mean,inplace=True)

MeanSal=df['Salary'].mean()
print(MeanSal)
df["Salary"].fillna(Mean,inplace=True)
print(df)

#3
#a)
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
labelencoder=LabelEncoder()
df['Country']=labelencoder.fit_transform(df['Country'])
print(df)

#b)
enc=OneHotEncoder(handle_unknown='ignore')
enc_df=pd.DataFrame(enc.fit_transform(df[['Purchased']]).toarray())
df=df.join(enc_df)
print(df)
