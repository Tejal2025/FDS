#SET A

#1
import numpy as np
data=np.array([[0,1],[2,3]])
print(data)
print("Expected Output")
print("Original flattened array:", np.array([[0,1],[2,3]]))
print("maximum value of the above flattened array:",np.max(data))
print("minimum value of the above flattened array:",np.min(data))

#2
import numpy as np
import scipy.stats as s
p1=[1,4,2]
p2=[3,4,6]
dist=np.linalg.norm(p1,p2)
print("Euclidian dist betwwen two points is:",dist)

#3
import pandas as pd
import scipy.stats as s
import numpy as np
data=np.array([18,29,40,37,44,90,77])
Mean=np.mean(data)
print("Mean:",Mean)
Range=(np.max(data)-np.min(data))
print("Range:",Range)
q3,q1=np.percentile(data,[75,25])
iqrvalue=q3-q1
print("iqr is:",iqrvalue)

#4
import numpy as np
def distsum(x,y,z):
    sum=0
    for i in range(n):
       for j in range(i+1,n):
          sum=sum+(abs(x[i]-x[j]))+(abs(y[i]-y[j]))
       return sum
x=[1,2,3,4,5]
y=[6,7,8,9,10]
n=len(x)
print("Manhattan distance is:",distsum(x,y,n))

#5
import numpy as np 
import matplotlib.pyplot as plt
nums=np.array([0.5,0.7,1.1,1.2,1.3,2.1])
bins=np.array([0,1,2,3])
plt.hist(nums,bins,color="blue",alpha=0.2)
plt.show()

#6
import pandas as pd
from matplotlib.pyplot import*
df=pd.DataFrame(columns=["name","age","percentage"])
df.loc[0]=["Tejal",18,90]
df.loc[1]=["Sanchi",19,95]
df.loc[2]=["Anjali",20,91]
df.loc[3]=["Nikita",21,85]
df.loc[4]=["Prachi",18,94]
df.loc[5]=["Neha",19,81]
df.loc[6]=["Sonali",20,89]
print(df)
print(df.describe())
