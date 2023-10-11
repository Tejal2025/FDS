import pandas as pd
import matplotlib.pyplot as plt
#q1
df=Iris(1).csv

df.plot(kind="scatter",x="PetalLengthCm",y="PetalWidthCm")
plt.show()
plt.bar(df["PertalLengthCm"],df["PetalWidthCm"])
plt.show()

#q2
df.plot(kind="scatter",x="SepalLengthCm",y="SepalWidthCm")
plt.show()
df.plot(kind="scatter",x="PetalLenthCm",y="PetalWidthCm")
plt.show()

#q3
import seaborn as sns
df=
data=df[["PetalLengthCm","PetalWidthCm","SepalLengthCm","SepalWidthCm"]]
data.boxplot()
plt.show()
