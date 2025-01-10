'''import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

df = pd.read_csv('/Users/jayj/Desktop/projects?/matplot/f1_racing_ML/F1_Constructor_Standings_2001_2023.csv')

data_2021 = df[df['Year']==2001]

x = df['Constructor']
y = df['Points']

plt.figure(figsize=(10,6))
plt.plot(x, y, data=data_2021)
plt.xlabel('Constructors')
plt.ylabel('Points')
plt.title('Constructor standing- 2001')
plt.xticks(rotation=45, ha='right')
plt.show()


# doesnt work'''

'''
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('f1_racing_ML/F1_Constructor_Standings_2001_2023.csv')

# Assuming df is your dataset
constructors = df['Constructor'].unique()
fig, ax = plt.subplots(figsize=(12, 6))

for constructor in constructors:
    subset = df[df['Constructor'] == constructor]
    ax.plot(subset['Year'], subset['Points'], label=constructor)

# Add labels, legend, and title
ax.set_xlabel('Year')
ax.set_ylabel('Points')
ax.set_title('Constructor Points Over Time (2001-2023)')
ax.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Put the legend outside the plot
plt.tight_layout()
plt.show()
'''



# this sums the point of all group or constructor and gives the final result
import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('f1_racing_ML/F1_Constructor_Standings_2001_2023.csv')

# Aggregate total points
constructor_totals = df.groupby('Constructor')['Points'].sum().reset_index()

# Bar chart
constructor_totals.sort_values(by='Points', ascending=False, inplace=True)
plt.figure(figsize=(10, 6))
plt.bar(constructor_totals['Constructor'], constructor_totals['Points'], color='skyblue')
plt.xlabel('Constructor')
plt.ylabel('Total Points')
plt.title('Total Constructor Points (2001-2023)')
plt.xticks(rotation=45)
plt.show()

