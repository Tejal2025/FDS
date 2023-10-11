#A1

import pandas as pd
import matplotlib.pyplot as plt
df=pd.DataFrame(columns=["name","age","percentage"])
df.loc[0]=["Tejal",18,90]
df.loc[1]=["Sanchi",19,95]
df.loc[2]=["Anjali",20,91]
df.loc[3]=["Nikita",21,85]
df.loc[4]=["Prachi",18,94]
df.loc[5]=["Neha",19,81]
df.loc[6]=["Sonali",20,89]
df.loc[7]=["Prerna",21,80]
df.loc[8]=["Mamta",18,79]
df.loc[9]=["Arpita",17,75]
print(df)

#A2
print("Shape of Data:",df.shape)
print("Number of rows and columns:",df.size)
print("Data type:",df.dtypes)
print("Description of Data:",df.describe())

#A4
df.loc[10]=["Sakshi",18,80]
df.loc[11]=["Roshni",17,81]
df.loc[12]=["Shital",19,72]
df.loc[13]=["Ashu",18,85]
df.loc[14]=["Snehal",19,84]
df["remark"]=None
print(df)
print(df.info())
print("Number of observation =",df.info())
print("Missing value =",df.isnull())
print("Duplicate value =",df.duplicated())

#A6
df.drop(columns="remark",axis=1,inplace=True)
print(df)
print(df.dropna())

#A7
#df.plot(x="name",y="percentage")
#plt.title("Line Plot")
#print(plt.show())

#A8
df.plot.scatter(x="name",y="percentage")
plt.title("Line Plot")
print(plt.show())
