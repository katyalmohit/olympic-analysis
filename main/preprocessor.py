import pandas as pd

df = pd.read_csv('../dataset/athlete_events.csv')
region_df = pd.read_csv('../dataset/noc_regions.csv')

def preprocess():
    global df, region_df
    
    # Filtering for summer olympics
    df = df[df['Season']=='Summer']
    
    # Merge with region_df
    df = df.merge(region_df, on = "NOC", how = 'left')
    
    # Dropping duplicates
    df.drop_duplicates(inplace = True)
    
    # One hot encoding medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis = 1)
    return df