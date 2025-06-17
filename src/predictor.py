'''
general strategy prediction based on starting compound using real Zandvoort data
author: mjwakex -  Marcus Elizondo-Darwin
'''

import pandas as pd
from collections import Counter
import argparse

# number of laps for dutch gp 
LAPS = 71

# time loss in pitlane avg (seconds)
TIME_LOSS = 22

# time loss in pitlane under saftey car or VSC (seonds)
TIME_LOSS_SC = 17

# read the dataset
df = pd.read_csv("../data/dataset.csv")


parser = argparse.ArgumentParser(description="Predict F1 strategy for Zandvoort.")
parser.add_argument('--compound', type=str, required=True, help='Starting tyre compound (SOFT, MEDIUM, HARD, INTERMEDIATE, WET)')

args = parser.parse_args()
starting_compound = args.compound.upper()

compounds = ["SOFT", "MEDIUM", "HARD", "INTERMEDIATE", "WET"]
if starting_compound not in compounds:
    print(f"Error: Invalid compound '{starting_compound}'. Valid options: {', '.join(compounds)}")
    exit(1)

# ensuring the dataframe is correctly sorted
df = df.sort_values(by=["Year", "Driver", "Stint"])

# filtering to only get the first stints
stint_1 = df[df["Stint"] == 1.0]


strategies = []

# get the strats for each driver
for (year, driver), group in df.groupby(['Year', 'Driver']):
    # sort by stint within each group
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
    pitlap_display = "END" if int(pitlap) == LAPS else int(pitlap)
    print(f"Stint {i + 1}: {compound}, pit lap = {pitlap_display}, stint length = {int(stint_len)}")
print(f"time loss in pitlane (avg) = {TIME_LOSS}s\ntotal time loss with this strat = {TIME_LOSS * len(most_common)}s")
print(f"time loss in pitlane under saftey car(avg) = {TIME_LOSS_SC}s\ntotal time loss with this strat with saftey car= {TIME_LOSS_SC * len(most_common)}s")
