
import seaborn as sns
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import datetime


df=pd.read_csv("earthquakes.csv")

df=df[df["eventtype"]=="earthquake"]

df=df.loc[:,['origintime','longitude',' latitude',' magnitude',' depth']]

df.to_csv("earthquake_clean.csv")

# 1. How many detectable earthquakes were there in your data?

df.shape[0]

# 2. Make a correlation matrix using proc corr of the variables. What is the relationship between magnitude and depth in your data?

cor=df.corr(method="pearson")

plt.figure(figsize=(14,10))
sns.heatmap(cor,vmin=0, vmax=1,annot=True, cmap="YlGnBu")
plt.savefig("correlationmatrix")
plt.show()

print("What is the relationship between magnitude and depth in your data?")
print(cor.iloc[2,3])

#3. Is there a correlation between latitude and longitude for this data? How can you interpret a correlation between these variables?

print("What is the relationship between latitude and longitude in your data?")
print(cor.iloc[1,0])

# 4. Is there a correlation between latitude and magnitude for this data? If so, what might this mean for the two main islands of New Zealand (North Island and South Island)?

print("Is there a correlation between latitude and magnitude for this data?")
print(cor.iloc[1,2])

print("Not a strong one, there is a very small negative correlation. Notice that the smaller the latitude the more south we are. This small correlation would mean that the smaller the latitude or the more south we are the higher the magnitude, but it's too small to be significant and considered as a strong relevant correlation")

plt.figure(figsize=(14,10))
plt.scatter(df.as_matrix([' latitude']),df.as_matrix([' magnitude']))
plt.show()

# 5. Describe missingness in the data. For the entire dataset, how many observations had at least one missing value for the variables of interest? What percentage of the data is missing

df=pd.read_csv("earthquakes.csv")

df.isnull().sum()

df.loc[:,["depthtype"]]

a=df[df["depthtype"]!="operator assigned"]

a.info()

# there are 324 earthquake who have NA in depthtype. There are also 3 observation who has 3 missing values for the variable evaluation status, meaning that the earthquake hasent been confirmed. 
# in total there are 324 observation with at least one missing values out of the 370 observation.

# 6. Make three plots which are time series of the earthquakes depths, magnitudes, and latitudes. (Here,
#you can plot the variable of interest against time.) Make the points connected by lines, as is typically
#done in time series plots

df=pd.read_csv("earthquakes.csv")

df=df[df["eventtype"]=="earthquake"]

df=df.loc[:,['origintime','longitude',' latitude',' magnitude',' depth']]

df.to_csv("earthquake_clean.csv")

b=df.as_matrix(['origintime'])

plt.figure(figsize=(16,10))
plt.title("depth time series")
plt.xlabel("time")
plt.ylabel("depth")
plt.plot(df.as_matrix(['origintime']),df.as_matrix([' depth']))
plt.savefig('depthtimeseries')
plt.show()


plt.figure(figsize=(16,10))
plt.title("magnitude time series")
plt.xlabel("time")
plt.ylabel("magnitude")
plt.plot(df.as_matrix(['origintime']),df.as_matrix([' magnitude']))
plt.savefig('magnitudetimeseries')
plt.show()

plt.figure(figsize=(16,10))
plt.title("latitude time series")
plt.xlabel("time")
plt.ylabel("latitude")
plt.plot(df.as_matrix(['origintime']),df.as_matrix([' latitude']))
plt.savefig('latitudetimeseries')
plt.show()

# 7. Make a plot of the latitude (y-axis) against longitude (x-axis) of the earthquakes and describe the plot

plt.figure(figsize=(14,10))
plt.scatter(df.as_matrix(['longitude']),df.as_matrix([' latitude']))
plt.savefig('latencyvslongitude')
plt.show()

# 8. Make a plot of the magnitude (y-axis) against depth (x-axis) of the earthquakes and describe the plot.


plt.figure(figsize=(14,10))
plt.scatter(df.as_matrix([' depth']),df.as_matrix([' magnitude']))
plt.xlabel("depth")
plt.ylabel("magnitude")
plt.title("Depth vs magnitude")
plt.savefig('depthvsmagnitude')
plt.show()

#9. Make a variable which is the time between successive earthquakes. Make a histogram of the times
#between earthquakes and describe the distribution.

temp=df.loc[1:,['origintime']]

tempo=df.loc[:368,['origintime']]

time=tempo-temp

plt.figure(figsize=(14,10))
np.histogram(time,bins=30)
plt.show()