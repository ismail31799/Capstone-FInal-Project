import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/ismailmustafa/Downloads/Stacked_Bar_Chart_Capstone_Project_Final.csv')

df.plot(kind='bar' , x='Year', stacked=True, figsize= (11,6));

plt.legend([], frameon=False)

plt.show()
