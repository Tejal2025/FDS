#SET B
#1
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("file:///data/ty8/Downloads/SOCR-HeightWeight.csv")
df.head(10)
df.tail(10)
df.sample(20)
print(df)

#2
print("Shape of dataframe:",df.shape)
print("Size of dataframe:",df.size)
print("Data type:",df.dtypes)

#3
print("Statistical Data:",df.describe())

#4
print("Number of observation:",df.info())
print("Missing values",df.isnull())

#5
df["BMI"]=(df["Weight(Pounds)"]/(df["Height(Inches)"]**2))
print(df)

#6
print("Maximum BMI :",df.BMI.max())
print("Minimum BMI :",df.BMI.min())

#7
df.plot.scatter(x="Height(Inches)",y="Weight(Pounds)")
plt.title("Scatter Diagram")
print(plt.show())
