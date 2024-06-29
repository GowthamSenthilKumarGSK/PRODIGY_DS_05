import pandas as pd
import matplotlib.pyplot as plt

# Load the accident dataset (replace with your actual file path)
accident_data = pd.read_csv("D:/PSG_Academics/TASK/Traffic_Accident.csv")

# Data Cleaning
# Handle missing values if any
accident_data.dropna(inplace=True)

# Colors for the bar plots
colors_road_surface = ['skyblue', 'salmon', 'lightgreen', 'lightcoral', 'gold']
colors_weather_conditions = ['lightblue', 'lightcoral', 'lightgreen', 'plum', 'gold']
colors_light_conditions = ['lightpink', 'lightblue', 'lightgreen', 'lightyellow', 'plum']
colors_accident_cause = ['skyblue', 'lightgreen', 'lightcoral', 'lightpink', 'lightyellow']

# Visualize distribution of variables

plt.figure(figsize=(12, 6))
accident_data['Road_surface_type'].value_counts().plot(kind='bar', color=colors_road_surface)
plt.title('Distribution of Road Surface Type')
plt.xlabel('Road Surface Type')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12, 6))
accident_data['Weather_conditions'].value_counts().plot(kind='bar', color=colors_weather_conditions)
plt.title('Distribution of Weather Conditions')
plt.xlabel('Weather Conditions')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12, 6))
accident_data['Light_conditions'].value_counts().plot(kind='bar', color=colors_light_conditions)
plt.title('Distribution of Light Conditions')
plt.xlabel('Light Conditions')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12, 6))
accident_data['Cause_of_accident'].value_counts().plot(kind='bar', color=colors_accident_cause)
plt.title('Distribution of Accident Causes')
plt.xlabel('Cause of Accident')
plt.ylabel('Number of Accidents')
plt.xticks(rotation=90)
plt.show()
