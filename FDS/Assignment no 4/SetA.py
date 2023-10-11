import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns

x=np.random.randn(50)

#Line chart
'''plt.plot(x)
plt.title("line chart")
plt.show()'''

#Scatter plot
'''plt.scatter(range(len(x)),x,color='m',marker='d')
plt.title("scatter plot")
plt.show()'''

#Histogram
'''plt.hist(x,color='black')
plt.title("Histogarm")
plt.show()'''

#Box plot
'''plt.boxplot(x,vert=False)
plt.title("Box Plot")
plt.show()'''

#Pie chart & Bar chart
'''t=[50,60,70,80,90]
s=["OS","FDS","PYTHON","CPP","BC"]
plt.pie(t,labels=s)

plt.bar(s,t)
plt.show()'''

#Iris
iris=sns.load_dataset("iris")
s=iris['species'].value_counts()
sns.barplot(x=s.index,y=s.values)
plt.show()

iris=sns.load_dataset("iris")
s=iris['species'].value_counts()
sns.pie(x=s.index,y=s.values)
plt.show()

