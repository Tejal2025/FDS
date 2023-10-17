import pandas as pd
import numpy as np
from sklearn import preprocessing
import scipy.stats as s

#1
df=pd.read_csv("file:///data/ty8/Ty%208/FDS/Assignment%20no%203/winequality-red.csv")
print(df)

#2
#Rescaling
print("Rescaling Data")
print("\n\n Data scaled between 0 and 1")
data_scaler=preprocessing.MinMaxScaler(feature_range=(0,1))
data_scaled =data_scaler.fit_transform(df)
print("\n Min Max Scaled data")
print("----------------------------------")
print(data_scaled.round(2))

#3
#Standardizing data
print("\n Standardizing Data")
print("--------------------")
arr=np.array(df)
print(arr)
print("\n initial mean=",s.tmean(arr),round(2))
print("\n initial standard devetion=",round(arr.std(),2))
X_scaled=preprocessing.scale(arr)
X_scaled.mean(axis=0)
X_scaled.std(axis=0)
print("\n standarding data=\n",X_scaled.round(2))
print("\n scaling mean :",s.tmean(X_scaled).round(2))
print("\n scaling standard deviation :",round(X_scaled.std(),2))

#4
#Normalizing Data
print("Normalization rescales such that sum of each row is 1:")
dn=preprocessing.normalize(df,norm='l1')
print("-------------------------------")
print(dn.round(2))

#5
#Binarizing Data
print("binarizer data(Make Binary)")
data_binarized=preprocessing.Binarizer(threshold=5).transform(df)
print("\n Binarized Data")
print("-----------------")
print(data_binarized)
