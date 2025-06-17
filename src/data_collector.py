'''
a data collector of rthe dutch gp using fastf1
author: mjwakex - Marcus Elizondo-Darwin
'''

import fastf1
from fastf1 import plotting

# cache directory
fastf1.Cache.enable_cache('../cache')

# we want the data from the races of the past 4 (2021) years since it was reintroduced to calendar
session_21 = fastf1.get_session(2021, "Netherlands", "R")
session_22 = fastf1.get_session(2022, "Netherlands", "R")
session_23 = fastf1.get_session(2023, "Netherlands", "R")
session_24 = fastf1.get_session(2024, "Netherlands", "R")

session_21.load()
session_22.load()
session_23.load()
session_24.load()

laps_21 = session_21.laps
laps_22 = session_22.laps
laps_23 = session_23.laps
laps_24 = session_24.laps

# adding year column manually to each dataframe
laps_21['Year'] = 2021
laps_22['Year'] = 2022
laps_23['Year'] = 2023
laps_24['Year'] = 2024

# getting the stint data (stint num, tyre compound, stint length) for each driver throughout each race
stints_21 = laps_21[["Year", "Driver", "Stint", "Compound", "LapNumber"]]
stints_21 = stints_21.groupby(["Year", "Driver", "Stint", "Compound"]).agg(
    PitLap = ("LapNumber", 'max'),
    StintLength = ("LapNumber", 'size')
).reset_index()

stints_22 = laps_22[["Year", "Driver", "Stint", "Compound", "LapNumber"]]
stints_22 = stints_22.groupby(["Year", "Driver", "Stint", "Compound"]).agg(
    PitLap = ("LapNumber", 'max'),
    StintLength = ("LapNumber", 'size')
).reset_index()

stints_23 = laps_23[["Year", "Driver", "Stint", "Compound", "LapNumber"]]
stints_23 = stints_23.groupby(["Year", "Driver", "Stint", "Compound"]).agg(
    PitLap = ("LapNumber", 'max'),
    StintLength = ("LapNumber", 'size')
).reset_index()

stints_24 = laps_24[["Year", "Driver", "Stint", "Compound", "LapNumber"]]
stints_24 = stints_24.groupby(["Year", "Driver", "Stint", "Compound"]).agg(
    PitLap = ("LapNumber", 'max'),
    StintLength = ("LapNumber", 'size')
).reset_index()

# print out stitn data from each loaded session
list_of_stints = [stints_21, stints_22, stints_23, stints_24]

def write_to_dataset(stint, filename="../data/dataset.csv", mode="a"):
    try: 
        stint.to_csv(filename, mode=mode, header=(mode=="w"), index=False)
    except Exception as e:
        print(f"Error writing to dataset: {e}")


for i, stints in enumerate(list_of_stints):
    print(stints)
    mode = "w" if i == 0 else "a"
    write_to_dataset(stints, mode=mode)


