import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Deaths Per Vehicle
dataIn = pd.read_csv("/Users/ismailmustafa/Downloads/Death Per Vehicle Smoothed.csv", header=None)

dataNP = dataIn.to_numpy()

x_axis = dataNP[:,0]
y_axis = dataNP[:,1]

plt.plot(x_axis,y_axis)
plt.title('Deaths per Vehicle in NYC')
plt.xlabel('Month of the Year')
plt.ylabel('Deaths Per Vehicle')
plt.xticks(rotation = 90)

plt.show()


#Deaths Per Accident
dataIn = pd.read_csv("/Users/ismailmustafa/Downloads/Deaths Per Accident Smoothed.csv", header=None)

dataNP = dataIn.to_numpy()

x_axis = dataNP[:,0]
y_axis = dataNP[:,1]

plt.plot(x_axis,y_axis)
plt.title('Deaths per Accident in NYC')
plt.xlabel('Month of the Year')
plt.ylabel('Deaths Per Accident')
plt.xticks(rotation = 90)

plt.show()


"""
dataIn = pd.read_csv("/Users/ismailmustafa/Downloads/Car Accident Rate Smoothed.csv", header=None)

dataNP = dataIn.to_numpy()

x_axis = dataNP[:,0]
y_axis = dataNP[:,1]

plt.plot(x_axis,y_axis)
plt.title('Accident Rate per Vehicle in NYC')
plt.xlabel('Month of the Year')
plt.ylabel('Accident Rate')
plt.xticks(rotation = 90)

plt.show()
"""
