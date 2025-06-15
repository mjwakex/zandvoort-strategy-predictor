import pandas as pd
from collections import Counter

# read the dataset
df = pd.read_csv("../data/dataset.csv")
# print(df.head())

# get the starting compound
valid = False
compounds = ["SOFT", "MEDIUM", "HARD", "INTERMEDIATE", "WET"]
while not valid:
    starting_compound = input("Starting Compound: ")
    if starting_compound in compounds:
        valid = True

# filtering to only get the first stints
stint_1 = df[df["Stint"] == 1.0]

# get all previoud strategies by driver
# print("Total races in raw data:", len(df.groupby(['Year', 'Driver'])))
strategies = df.groupby(['Year', 'Driver']).agg(list).reset_index()
# print("Total rows in strategy list:", len(strategies))


# filter strategies based on starting compound
filtered_strats = strategies[strategies["Compound"].str[0] == starting_compound]

# find most common second and third stints
compound_strats = []
for stints in filtered_strats["Compound"]:
    compound_strats.append(tuple(stints))

strategy_counts = Counter(compound_strats)
most_common = strategy_counts.most_common(1)[0][0]

print("\nFull strategy breakdown:")
for i, compound in enumerate(most_common):
    print(f"Stint {i + 1}: {compound}")