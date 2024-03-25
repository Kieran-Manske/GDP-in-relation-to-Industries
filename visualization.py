import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel("C:/Users/kmanske343/Documents/GitHub/GDP-in-relation-to-Industries/SAGDP2N__ALL_AREAS_1997_2022_cleaned.xlsx")

df.columns = df.columns.str.strip()
df['Description'] = df['Description'].str.strip()
df['GeoName'] = df['GeoName'].str.strip()

all_years =[x for x in range(1997, 2022)]


years_df = pd.DataFrame(all_years)
years_df.head(5)
#join years_df with df
df = df.join(years_df)

industries = df['Description'].unique()
print(len(industries))

def state_of_choice(df, State):
    
    state_df = df.loc[df['GeoName'] == State]
    state_df = state_df.set_index('Description')
    return state_df

for state in df['GeoName'].unique():
    if state == 'United States *':
        continue
    state_df = state_of_choice(df, state)
    state_df.to_csv(f'{state}.csv')
    print(f'{state} has been saved to a csv file')




#turn this dataframe into a text file csv
