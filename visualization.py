import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel("C:/Users/kmanske343/Documents/GitHub/GDP-in-relation-to-Industries/SAGDP2N__ALL_AREAS_1997_2022_cleaned.xlsx")


industries = df['Description'].unique()
print(len(industries))

def state_of_choice(df, State):
    
    state_df = df.loc[df['GeoName'] == State]
    state_df = state_df.set_index('Description')
    print(state_df)

state_of_choice(df, 'Alabama')


