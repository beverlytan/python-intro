# Coding club: Intro to Python
# Beverly / 16 Feb 2019

## Using basic Python commands to extract a specific line

# pressure_data = []

# with open("StormEleanor_2_3_Jan.csv", "r") as weatherfile:
#     next(weatherfile)
#     for line in weatherfile:
#         data_row = line.split(',')
#         pressure = data_row[6]
#         pressure_data.append(float(pressure))
    
# print(pressure_data[0])
# type(pressure_data[1])

## Learning to use pandas to load in data

import pandas as pd

data = pd.read_csv("StormEleanor_2_3_Jan.csv", delimiter = ",", header = 0)

print(data.head(1))

pressure_data = data['Pair_Avg']

print(pressure_data)

## Importing data into matplotlib

import matplotlib.pyplot as plt 

# plt.plot(pressure_data)
# plt.ylabel("Pressure / hPa")
# plt.title("Pressure measurements, JCMB Weather Station: 2 - 3 Jan 2018")

# Create ACTUAL timeseries values instead of 
# x data being integers for each timestep 

import datetime

date_timeseries = []
date_time = datetime.datetime(2018, 1, 2)
date_at_end = datetime.datetime(2018, 1, 3, 23, 59)
step = datetime.timedelta(minutes = 1)

while date_time <= date_at_end: 
    date_timeseries.append(date_time)
    date_time += step
    
plt.plot(date_timeseries, pressure_data)
plt.ylabel("Pressure / hPa")
plt.xlabel("Time")
plt.title("Pressure measurements, JCMB Weather Station: 2 - 3 Jan 2018")
plt.xticks(rotation = 30)

plt.tight_layout()

plt.savefig("cc-intro-python-pressure.jpg")