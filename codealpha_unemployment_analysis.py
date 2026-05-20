# Unemployment Analysis using Python

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
# Replace 'Unemployment.csv' with your dataset file name
data = pd.read_csv('Unemployment.csv')

# Display first 5 rows
print("Dataset Preview:\n")
print(data.head())

# Check missing values
print("\nMissing Values:\n")
print(data.isnull().sum())

# Basic information
print("\nDataset Info:\n")
print(data.info())

# Describe data
print("\nStatistical Summary:\n")
print(data.describe())

# Convert Date column into datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Plot unemployment rate over time
plt.figure(figsize=(10,5))
plt.plot(data['Date'], data['Estimated Unemployment Rate (%)'])

# Labels and title
plt.title('Unemployment Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')

# Rotate dates
plt.xticks(rotation=45)

# Show graph
plt.tight_layout()
plt.show()

# Average unemployment rate
average_rate = data['Estimated Unemployment Rate (%)'].mean()

print("\nAverage Unemployment Rate:", average_rate)
