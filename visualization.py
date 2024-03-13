import pandas as pd
import matplotlib.pyplot as plt
file = pd.read_excel('SAGDP2N_ALL_AREAS_1997_2022_cleaned.xlsx') 

#create a list of lists to store the data for every idustry in every state
state_data = []
for state in file['GeoName'].unique():
    state_data.append(file['GeoName'] == state)
    


