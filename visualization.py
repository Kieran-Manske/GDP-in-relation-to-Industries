import pandas as pd
import matplotlib.pyplot as plt

#read the data from the excel file
df = pd.read_excel('C:\Users\kmanske343\Documents\GitHub\GDP-in-relation-to-Industries\SAGDP2N__ALL_AREAS_1997_2022_cleaned.xlsx')

#plot the data
df.plot(x='Year', y='GDP', kind='line')
plt.show()
