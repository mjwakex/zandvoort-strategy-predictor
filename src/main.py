'''
A pit stop predictor for the dutch gp
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

# getting the stint data for each driver trhoughout the race
stints_21 = laps_21[["Driver", "Stint", "Compound", "LapNumber"]]
stints_21 = stints_21.groupby(["Driver", "Stint", "Compound"])
stints_21 = stints_21.count().reset_index()

stints_22 = laps_22[["Driver", "Stint", "Compound", "LapNumber"]]
stints_22 = stints_22.groupby(["Driver", "Stint", "Compound"])
stints_22 = stints_22.count().reset_index()

stints_23 = laps_23[["Driver", "Stint", "Compound", "LapNumber"]]
stints_23 = stints_23.groupby(["Driver", "Stint", "Compound"])
stints_23 = stints_23.count().reset_index()

stints_24 = laps_24[["Driver", "Stint", "Compound", "LapNumber"]]
stints_24 = stints_24.groupby(["Driver", "Stint", "Compound"])
stints_24 = stints_24.count().reset_index()
