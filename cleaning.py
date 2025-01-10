import pandas as pd
import numpy as np
df = pd.read_csv('/Users/jayj/Desktop/projects?/matplot/f1_racing_ML/f1_race_weather_2020_2023.csv')
df['Latitude']=df['Latitude'].round(3)
df['Longitude']=df['Longitude'].round(3)


# Replace 'unknown' randomly based on probabilities                     ---> this not working because  .replace() method in pandas is not designed to work with np.random.choice() in this way.
'''def change_unknown(df, dry_count, wet_count):            
    total = dry_count+wet_count
    dry_prob = dry_count/total
    wet_prob = wet_count/total
    df['Weather'] = df['Weather'].replace('unknown', np.random.choice(['dry', 'wet'], size=df['Weather'].value_counts()['unknown'], p=[dry_prob, wet_prob]))
    return df


dry_count = df['Weather'].value_counts().get('dry', 0)
wet_count = df['Weather'].value_counts().get('wet', 0)


new_df = change_unknown(df, dry_count, wet_count)
print(new_df.to_string())'''


def change_unknown(df, dry_count, wet_count):
    total = dry_count+wet_count
    dry_prob = dry_count/total
    wet_prob = wet_count/total
     
    for x in df.index:
        if df.loc[x, 'Weather'] == 'unknown':
            df.loc[x, 'Weather'] = np.random.choice(['dry', 'wet'], p=[dry_prob, wet_prob])
    return df

dry_count = df['Weather'].value_counts().get('dry', 0)
wet_count = df['Weather'].value_counts().get('wet', 0)

updated_df = change_unknown(df, dry_count, wet_count)
print(updated_df.to_string())