#SET B
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("file:///data/ty8/Downloads/SOCR-HeightWeight.csv")
df.head(10)
df.tail(10)
df.sample(20)
print(df)

print("Shape of dataframe:",df.shape)
print("Size of dataframe:",df.size)
print("Data type:",df.dtypes)
print("Statistical Data:",df.describe())
print("Number of observation:",df.info())
print("Missing values",df.isnull())
df["BMI"]=(df["Weight(Pounds)"]/(df["Height(Inches)"]**2))
print(df)

print("Maximum BMI :",df.BMI.max())
print("Minimum BMI :",df.BMI.min())

df.plot.scatter(x="Height(Inches)",y="Weight(Pounds)")
plt.title("Scatter Diagram")
print(plt.show())
