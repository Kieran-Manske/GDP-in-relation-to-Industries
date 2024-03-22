import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel("C:/Users/kmanske343/Documents/GitHub/GDP-in-relation-to-Industries/SAGDP2N__ALL_AREAS_1997_2022_cleaned.xlsx")

df.columns = df.columns.str.strip()
df['Description'] = df['Description'].str.strip()




industries = df['Description'].unique()
print(len(industries))

def state_of_choice(df, State):
    
    state_df = df.loc[df['GeoName'] == State]
    state_df = state_df.set_index('Description')
    return state_df



print(state_of_choice(df, 'Alabama'))

state_df = state_of_choice(df, 'Alabama')

def plot_data(state_df, State, Industry):
    state_df = state_df.loc[Industry]
    state_df = state_df.iloc[2:]
    print(state_df)
    state_df.plot(kind = 'bar', x = 'Years' , y = 'Trade in millions',
                  title = f'{Industry} in {State}',
                  legend = False)
    plt.show()

plot_data(state_df, 'Alabama', 'Trade')