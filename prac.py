#To read the dataset
import pandas as pd 

#For visualization
import matplotlib.pyplot as plt
#Read the dataset

path = '/Users/hb/Desktop/Uber/uber-raw-data.csv'
uber_df = pd.read_csv('/Users/hb/Desktop/Uber/uber-raw-data.csv')

#Display the first 5 records
print(uber_df.head(5))
#Display the last 5 records
print(uber_df.tail())
#Find the shape of the dataset
print(uber_df.shape)
#Understand the dataset properties
print(uber_df.info())
#Change the "Date/Time" column's data type from string to datetime
uber_df['Date/Time']= pd.to_datetime(uber_df['Date/Time'])

#Convert "Date/Time" column from string data type into DateTime
uber_df["Day"] = uber_df["Date/Time"].apply(lambda x: x.day)
uber_df["Hour"] = uber_df["Date/Time"].apply(lambda x: x.hour)
uber_df["Weekday"] = uber_df["Date/Time"].apply(lambda x: x.weekday())
print(uber_df.head(5))
#Visualize the Density of rides per Day of month
fig, ax = plt.subplots(figsize=(12, 6))

# Create the histogram
ax.hist(uber_df['Day'], width=0.6, bins=30)

# Add labels and a title
ax.set_title('Density of trips per Day', fontsize=16)
ax.set_xlabel('Day', fontsize=14)
ax.set_ylabel('Density of rides', fontsize=14)

# Show the plot
plt.show()
#Visualize the Density of rides per Weekday
fig,ax = plt.subplots(figsize = (12,6))
plt.hist(uber_df.Weekday, width= 0.4, range= (0, 6.5), bins=7, color= "green")
plt.title("Density of trips per Weekday", fontsize=16)
plt.xlabel("Weekday", fontsize=14)
plt.ylabel("Density of rides", fontsize=14)
plt.show()
#Highest number of rides are during working days(Monday to Friday),while the least number of rides are during weekend.

#Visualize the Density of rides per hour
fig,ax = plt.subplots(figsize = (12,6))
plt.hist(uber_df.Hour, width= 0.6, bins=24, color= "orange")
plt.title("Density of trips per Hour", fontsize=16)
plt.xlabel("Hour", fontsize=14)
plt.ylabel("Density of rides", fontsize=14)
plt.show()
#The busiest day in the week for Uber is Moday.Saturday is the day with least number of rides.

#Visualize the Density of rides per location
fig,ax = plt.subplots(figsize = (12,6))
x= uber_df.Lon
y= uber_df.Lat
plt.scatter(x, y, color= "purple")
plt.title("Density of trips per Hour", fontsize=16)
plt.xlabel("Hour", fontsize=14)
plt.ylabel("Density of rides", fontsize=14)
plt.show()
#It seems like number of rides decrease gradually from 1 am to 4 am and then starts increasing from 5 am till 6pm which is the hour with highest number of rides.




