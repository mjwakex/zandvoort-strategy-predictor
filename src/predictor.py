import pandas as pd
from collections import Counter

# number of laps for dutch gp 
LAPS = 71

# read the dataset
df = pd.read_csv("../data/dataset.csv")


# get the starting compound
valid = False
compounds = ["SOFT", "MEDIUM", "HARD", "INTERMEDIATE", "WET"]
while not valid:
    starting_compound = input("Starting Compound: ").upper()
    if starting_compound in compounds:
        valid = True

# ensuring the dataframe is correctly sorted
df = df.sort_values(by=["Year", "Driver", "Stint"])

# filtering to only get the first stints
stint_1 = df[df["Stint"] == 1.0]


# get all previoud strategies by driver
# driver_strategies = df.groupby(['Year', 'Driver']).agg(list).reset_index()

strategies = []

for (year, driver), group in df.groupby(['Year', 'Driver']):
    # Sort by stint within each group
    group = group.sort_values(by='Stint')
    compound_list = group['Compound'].tolist()
    pitlap_list = group['PitLap'].tolist()
    length_list = group['StintLength'].tolist()

    # filtering based on starting compound
    if compound_list and compound_list[0] == starting_compound:
        strategy = list(zip(compound_list, pitlap_list, length_list))
        strategies.append(strategy)



# count most common strategy
strategy_counts = Counter(tuple(s) for s in strategies)
most_common = strategy_counts.most_common(1)[0][0]

# output result
print("\nFull strategy breakdown:")
for i, (compound, pitlap, stint_len) in enumerate(most_common):
    # replace pit lap with FIN if last lap 
    pitlap_display = "FIN" if int(pitlap) == LAPS else int(pitlap)
    print(f"Stint {i + 1}: {compound}, pit lap = {pitlap_display}, stint length = {int(stint_len)}")
