#Import Necessary Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define the path to your CSV file
csv_path = r'C:\Users\Owner\Desktop\Grad School\Repository\Garrison\data\Python\fatal-police-shootings-agencies.csv'

# Load the data into a DataFrame
df = pd.read_csv(csv_path)

# Display the first few rows to inspect the data
print(df.head())

# Create a bar plot of the number of fatal police shootings by state
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='state', order=df['state'].value_counts().index, palette='viridis')
plt.xlabel('State')
plt.ylabel('Number of Fatal Shootings')
plt.title('Fatal Police Shootings by State')
plt.xticks(rotation=90)
plt.tight_layout()

# Show the plot
plt.show()
