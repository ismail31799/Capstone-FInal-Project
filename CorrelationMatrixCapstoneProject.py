import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/ismailmustafa/Downloads/Motor_Vehicle_Collisions_-_Crashes.csv")
#pd.options.display.max_columns = None
#df = np.array(df)

df_essentials = df.drop(['ZIP CODE', 'LATITUDE', 'LONGITUDE', 'LOCATION', 'ON STREET NAME', 'CROSS STREET NAME', 'OFF STREET NAME', 'COLLISION_ID', "VEHICLE TYPE CODE 1", "VEHICLE TYPE CODE 2", "VEHICLE TYPE CODE 3", "VEHICLE TYPE CODE 4", "VEHICLE TYPE CODE 5"], axis=1)
df_essentials['Total Injured'] = df_essentials['NUMBER OF PERSONS INJURED'] + df_essentials['NUMBER OF PEDESTRIANS INJURED'] + df_essentials['NUMBER OF CYCLIST INJURED'] + df_essentials['NUMBER OF MOTORIST INJURED']
df_essentials['Total Killed'] = df_essentials['NUMBER OF PERSONS KILLED'] + df_essentials['NUMBER OF PEDESTRIANS KILLED'] + df_essentials['NUMBER OF CYCLIST KILLED'] + df_essentials['NUMBER OF MOTORIST KILLED']
#for col in df_essentials:
#   print(col, ":", df[col].unique())

#for col in df_essentials.columns:
#    print(col)

#print(df_essentials.BOROUGH)

df_essentials["CRASH HOUR"] = df_essentials["CRASH TIME"].str[0:2]
df_essentials["CRASH HOUR"] = df_essentials["CRASH HOUR"].str.replace('\:', '')
df_essentials = df_essentials.drop(['CRASH TIME'], axis=1)

grouped_df_inj_kil = df_essentials.groupby(['CRASH DATE'], sort = False, as_index =False)['Total Injured', 'Total Killed'].sum()
grouped_df_inj_kil = grouped_df_inj_kil.rename(columns={"CRASH DATE": "Date"})

#print(grouped_df_inj_kil)

#grouped_df = df_essentials.groupby(['CRASH DATE'], sort = False, as_index =False)['CRASH DATE'].count()
grouped_df = df_essentials.groupby(['CRASH DATE'], sort = False, as_index = False).size()
#grouped_df = grouped_df.to_frame()

#grouped_df = grouped_df({'Total Accidents': df_essentials.groupby(["CRASH DATE"]).size()}).reset_index()

grouped_df = grouped_df.reset_index(name='Total Accidents')
grouped_df = grouped_df.rename(columns={"CRASH DATE": "Date"})
#print(grouped_df)

merged_df = pd.merge(grouped_df_inj_kil, grouped_df, on='Date')
print(merged_df)

#df_essentials['Total Injured'] = df_essentials['NUMBER OF PERSONS INJURED'] + df_essentials['NUMBER OF PEDESTRIANS INJURED'] + df_essentials['NUMBER OF CYCLIST INJURED'] + df_essentials['NUMBER OF MOTORIST INJURED']
#df_essentials['Total Killed'] = df_essentials['NUMBER OF PERSONS KILLED'] + df_essentials['NUMBER OF PEDESTRIANS KILLED'] + df_essentials['NUMBER OF CYCLIST KILLED'] + df_essentials['NUMBER OF MOTORIST KILLED']

#df_final = df_essentials.groupby(['Crash Date'], sort = False, as_index =False)['Total Vehicles'].sum()


#Converting to Numeric
df_essentials["BOROUGH"] = df_essentials["BOROUGH"].map({"BRONX": 1, "BROOKLYN": 2, "QUEENS": 3, "MANHATTAN": 4, "STATEN ISLAND": 5})
df_essentials["CONTRIBUTING FACTOR VEHICLE 1"] = df_essentials["CONTRIBUTING FACTOR VEHICLE 1"].map({'Following Too Closely': 1, 'Unspecified': 2, 'Pavement Slippery': 3, 'Driver Inattention/Distraction': 4, 'Other Vehicular': 5, 'Passing Too Closely': 6, 'Passing or Lane Usage Improper': 7, 'Driver Inexperience': 8, 'Failure to Yield Right-of-Way': 9, 'Brakes Defective': 10, 'Turning Improperly': 11, 'Unsafe Speed': 12, 'Backing Unsafely': 13, 'Reaction to Uninvolved Vehicle': 14, 'View Obstructed/Limited': 15, 'Steering Failure': 16, 'Traffic Control Disregarded': 17, 'Drugs (illegal)': 18, 'Aggressive Driving/Road Rage': 19, 'Fell Asleep': 20, 'Pedestrian/Bicyclist/Other Pedestrian Error/Confusion': 21, 'Alcohol Involvement': 22, 'Unsafe Lane Changing': 23, 'Pavement Defective': 24, 'Other Lighting Defects': 25, 'Animals Action': 26, 'Outside Car Distraction': 27, 'Illnes': 28, 'Driverless/Runaway Vehicle': 29, 'Passenger Distraction': 30, 'Tire Failure/Inadequate': 31, 'Lost Consciousness': 32, 'Accelerator Defective': 33, 'Obstruction/Debris': 34, 'Failure to Keep Right': 35, 'Glare': 36, 'Eating or Drinking': 37, 'Cell Phone (hands-free)': 38, 'Lane Marking Improper/Inadequate': 39, 'Using On Board Navigation Device': 40, 'Fatigued/Drowsy': 41, 'Tow Hitch Defective': 42, 'Physical Disability': 43, 'Cell Phone (hand-Held)': 44, 'Headlights Defective': 45, 'Tinted Windows': 46, 'Vehicle Vandalism': 47, 'Prescription Medication': 48, 'Listening/Using Headphones': 49, 'Texting': 50, 'Traffic Control Device Improper/Non-Working': 51, 'Other Electronic Device': 52, 'Windshield Inadequate': 53, 'Shoulders Defective/Improper': 54, '80': 0, 'Reaction to Other Uninvolved Vehicle': 55, '1': 0, 'Drugs (Illegal)': 56, 'Illness': 57, 'Cell Phone (hand-held)': 58, 'Oversized Vehicle': 59})
df_essentials["CONTRIBUTING FACTOR VEHICLE 2"] = df_essentials["CONTRIBUTING FACTOR VEHICLE 2"].map({'Following Too Closely': 1, 'Unspecified': 2, 'Pavement Slippery': 3, 'Driver Inattention/Distraction': 4, 'Other Vehicular': 5, 'Passing Too Closely': 6, 'Passing or Lane Usage Improper': 7, 'Driver Inexperience': 8, 'Failure to Yield Right-of-Way': 9, 'Brakes Defective': 10, 'Turning Improperly': 11, 'Unsafe Speed': 12, 'Backing Unsafely': 13, 'Reaction to Uninvolved Vehicle': 14, 'View Obstructed/Limited': 15, 'Steering Failure': 16, 'Traffic Control Disregarded': 17, 'Drugs (illegal)': 18, 'Aggressive Driving/Road Rage': 19, 'Fell Asleep': 20, 'Pedestrian/Bicyclist/Other Pedestrian Error/Confusion': 21, 'Alcohol Involvement': 22, 'Unsafe Lane Changing': 23, 'Pavement Defective': 24, 'Other Lighting Defects': 25, 'Animals Action': 26, 'Outside Car Distraction': 27, 'Illnes': 28, 'Driverless/Runaway Vehicle': 29, 'Passenger Distraction': 30, 'Tire Failure/Inadequate': 31, 'Lost Consciousness': 32, 'Accelerator Defective': 33, 'Obstruction/Debris': 34, 'Failure to Keep Right': 35, 'Glare': 36, 'Eating or Drinking': 37, 'Cell Phone (hands-free)': 38, 'Lane Marking Improper/Inadequate': 39, 'Using On Board Navigation Device': 40, 'Fatigued/Drowsy': 41, 'Tow Hitch Defective': 42, 'Physical Disability': 43, 'Cell Phone (hand-Held)': 44, 'Headlights Defective': 45, 'Tinted Windows': 46, 'Vehicle Vandalism': 47, 'Prescription Medication': 48, 'Listening/Using Headphones': 49, 'Texting': 50, 'Traffic Control Device Improper/Non-Working': 51, 'Other Electronic Device': 52, 'Windshield Inadequate': 53, 'Shoulders Defective/Improper': 54, '80': 0, 'Reaction to Other Uninvolved Vehicle': 55, '1': 0, 'Drugs (Illegal)': 56, 'Illness': 57, 'Cell Phone (hand-held)': 58, 'Oversized Vehicle': 59})
df_essentials["CONTRIBUTING FACTOR VEHICLE 3"] = df_essentials["CONTRIBUTING FACTOR VEHICLE 3"].map({'Following Too Closely': 1, 'Unspecified': 2, 'Pavement Slippery': 3, 'Driver Inattention/Distraction': 4, 'Other Vehicular': 5, 'Passing Too Closely': 6, 'Passing or Lane Usage Improper': 7, 'Driver Inexperience': 8, 'Failure to Yield Right-of-Way': 9, 'Brakes Defective': 10, 'Turning Improperly': 11, 'Unsafe Speed': 12, 'Backing Unsafely': 13, 'Reaction to Uninvolved Vehicle': 14, 'View Obstructed/Limited': 15, 'Steering Failure': 16, 'Traffic Control Disregarded': 17, 'Drugs (illegal)': 18, 'Aggressive Driving/Road Rage': 19, 'Fell Asleep': 20, 'Pedestrian/Bicyclist/Other Pedestrian Error/Confusion': 21, 'Alcohol Involvement': 22, 'Unsafe Lane Changing': 23, 'Pavement Defective': 24, 'Other Lighting Defects': 25, 'Animals Action': 26, 'Outside Car Distraction': 27, 'Illnes': 28, 'Driverless/Runaway Vehicle': 29, 'Passenger Distraction': 30, 'Tire Failure/Inadequate': 31, 'Lost Consciousness': 32, 'Accelerator Defective': 33, 'Obstruction/Debris': 34, 'Failure to Keep Right': 35, 'Glare': 36, 'Eating or Drinking': 37, 'Cell Phone (hands-free)': 38, 'Lane Marking Improper/Inadequate': 39, 'Using On Board Navigation Device': 40, 'Fatigued/Drowsy': 41, 'Tow Hitch Defective': 42, 'Physical Disability': 43, 'Cell Phone (hand-Held)': 44, 'Headlights Defective': 45, 'Tinted Windows': 46, 'Vehicle Vandalism': 47, 'Prescription Medication': 48, 'Listening/Using Headphones': 49, 'Texting': 50, 'Traffic Control Device Improper/Non-Working': 51, 'Other Electronic Device': 52, 'Windshield Inadequate': 53, 'Shoulders Defective/Improper': 54, '80': 0, 'Reaction to Other Uninvolved Vehicle': 55, '1': 0, 'Drugs (Illegal)': 56, 'Illness': 57, 'Cell Phone (hand-held)': 58, 'Oversized Vehicle': 59})
df_essentials["CONTRIBUTING FACTOR VEHICLE 4"] = df_essentials["CONTRIBUTING FACTOR VEHICLE 4"].map({'Following Too Closely': 1, 'Unspecified': 2, 'Pavement Slippery': 3, 'Driver Inattention/Distraction': 4, 'Other Vehicular': 5, 'Passing Too Closely': 6, 'Passing or Lane Usage Improper': 7, 'Driver Inexperience': 8, 'Failure to Yield Right-of-Way': 9, 'Brakes Defective': 10, 'Turning Improperly': 11, 'Unsafe Speed': 12, 'Backing Unsafely': 13, 'Reaction to Uninvolved Vehicle': 14, 'View Obstructed/Limited': 15, 'Steering Failure': 16, 'Traffic Control Disregarded': 17, 'Drugs (illegal)': 18, 'Aggressive Driving/Road Rage': 19, 'Fell Asleep': 20, 'Pedestrian/Bicyclist/Other Pedestrian Error/Confusion': 21, 'Alcohol Involvement': 22, 'Unsafe Lane Changing': 23, 'Pavement Defective': 24, 'Other Lighting Defects': 25, 'Animals Action': 26, 'Outside Car Distraction': 27, 'Illnes': 28, 'Driverless/Runaway Vehicle': 29, 'Passenger Distraction': 30, 'Tire Failure/Inadequate': 31, 'Lost Consciousness': 32, 'Accelerator Defective': 33, 'Obstruction/Debris': 34, 'Failure to Keep Right': 35, 'Glare': 36, 'Eating or Drinking': 37, 'Cell Phone (hands-free)': 38, 'Lane Marking Improper/Inadequate': 39, 'Using On Board Navigation Device': 40, 'Fatigued/Drowsy': 41, 'Tow Hitch Defective': 42, 'Physical Disability': 43, 'Cell Phone (hand-Held)': 44, 'Headlights Defective': 45, 'Tinted Windows': 46, 'Vehicle Vandalism': 47, 'Prescription Medication': 48, 'Listening/Using Headphones': 49, 'Texting': 50, 'Traffic Control Device Improper/Non-Working': 51, 'Other Electronic Device': 52, 'Windshield Inadequate': 53, 'Shoulders Defective/Improper': 54, '80': 0, 'Reaction to Other Uninvolved Vehicle': 55, '1': 0, 'Drugs (Illegal)': 56, 'Illness': 57, 'Cell Phone (hand-held)': 58, 'Oversized Vehicle': 59})
df_essentials["CONTRIBUTING FACTOR VEHICLE 5"] = df_essentials["CONTRIBUTING FACTOR VEHICLE 5"].map({'Following Too Closely': 1, 'Unspecified': 2, 'Pavement Slippery': 3, 'Driver Inattention/Distraction': 4, 'Other Vehicular': 5, 'Passing Too Closely': 6, 'Passing or Lane Usage Improper': 7, 'Driver Inexperience': 8, 'Failure to Yield Right-of-Way': 9, 'Brakes Defective': 10, 'Turning Improperly': 11, 'Unsafe Speed': 12, 'Backing Unsafely': 13, 'Reaction to Uninvolved Vehicle': 14, 'View Obstructed/Limited': 15, 'Steering Failure': 16, 'Traffic Control Disregarded': 17, 'Drugs (illegal)': 18, 'Aggressive Driving/Road Rage': 19, 'Fell Asleep': 20, 'Pedestrian/Bicyclist/Other Pedestrian Error/Confusion': 21, 'Alcohol Involvement': 22, 'Unsafe Lane Changing': 23, 'Pavement Defective': 24, 'Other Lighting Defects': 25, 'Animals Action': 26, 'Outside Car Distraction': 27, 'Illnes': 28, 'Driverless/Runaway Vehicle': 29, 'Passenger Distraction': 30, 'Tire Failure/Inadequate': 31, 'Lost Consciousness': 32, 'Accelerator Defective': 33, 'Obstruction/Debris': 34, 'Failure to Keep Right': 35, 'Glare': 36, 'Eating or Drinking': 37, 'Cell Phone (hands-free)': 38, 'Lane Marking Improper/Inadequate': 39, 'Using On Board Navigation Device': 40, 'Fatigued/Drowsy': 41, 'Tow Hitch Defective': 42, 'Physical Disability': 43, 'Cell Phone (hand-Held)': 44, 'Headlights Defective': 45, 'Tinted Windows': 46, 'Vehicle Vandalism': 47, 'Prescription Medication': 48, 'Listening/Using Headphones': 49, 'Texting': 50, 'Traffic Control Device Improper/Non-Working': 51, 'Other Electronic Device': 52, 'Windshield Inadequate': 53, 'Shoulders Defective/Improper': 54, '80': 0, 'Reaction to Other Uninvolved Vehicle': 55, '1': 0, 'Drugs (Illegal)': 56, 'Illness': 57, 'Cell Phone (hand-held)': 58, 'Oversized Vehicle': 59})
df_essentials["CRASH HOUR"] = df_essentials["CRASH HOUR"].map({'5': 5, '21': 21, '16': 16, '8': 8, '17': 17, '23': 23, '20': 20, '11': 11, '22': 22, '15': 15, '14': 14, '13': 13, '0': 0, '10': 10, '18': 18, '19': 19, '12': 12, '1': 1, '3': 3, '6': 6, '7': 7, '9': 9, '2': 2, '4': 4})
#print(df_essentials["CRASH TIME"].unique())
#print(df_essentials["CRASH HOUR"].unique())
#print(df_essentials["CONTRIBUTING FACTOR VEHICLE 1"].unique())
#print(df_essentials["CONTRIBUTING FACTOR VEHICLE 2"].unique())
#print(df_essentials["CONTRIBUTING FACTOR VEHICLE 3"].unique())
#print(df_essentials["CONTRIBUTING FACTOR VEHICLE 4"].unique())
#print(df_essentials["CONTRIBUTING FACTOR VEHICLE 5"].unique())
#print(df_essentials["BOROUGH"])
#print(df_essentials["CONTRIBUTING FACTOR VEHICLE 1"])
df_essentials = df_essentials.fillna(0)

print(df_essentials.corr())


plt.figure(figsize=(16, 6))
heatmap = sns.heatmap(df_essentials.corr(), vmin=-1, vmax=1, annot=True)
heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':12}, pad=12);

