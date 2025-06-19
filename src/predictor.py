'''
general strategy prediction based on starting compound using real Zandvoort data
author: mjwakex -  Marcus Elizondo-Darwin
'''

import pandas as pd
from collections import Counter
import argparse

# number of laps for dutch gp, standard is 72 but some of the data is a little inconsistent (71)
LAPS = {71, 72}

# time loss in pitlane avg (seconds)
TIME_LOSS = 22

# time loss in pitlane under saftey car or VSC (seonds)
TIME_LOSS_SC = 17

# read the dataset
df = pd.read_csv("data/dataset.csv")

# taking arguments in the command line, either give compund XOR driver
parser = argparse.ArgumentParser(description="Predict F1 strategy for Zandvoort.")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('--compound', type=str, help='Starting tyre compound (SOFT, MEDIUM, HARD, INTERMEDIATE, WET)')
group.add_argument('--driver', type=str, help='Driver alias (VER, LEC, HAM)')

args = parser.parse_args()


# ensuring the dataframe is correctly sorted
df = df.sort_values(by=["Year", "Driver", "Stint"])

strategies = []

if args.compound:
    starting_compound = args.compound.upper()

    compounds = ["SOFT", "MEDIUM", "HARD", "INTERMEDIATE", "WET"]
    if starting_compound not in compounds:
        print(f"Error: Invalid compound '{starting_compound}'. Valid options: {', '.join(compounds)}")
        exit(1)
    
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

elif args.driver:
    selected_driver = args.driver.upper()

    available_drivers = sorted(df["Driver"].unique())
    if selected_driver not in available_drivers:
        print(f"Error: Invalid driver '{selected_driver}'. Available drivers: {', '.join(available_drivers)}")
        exit(1)
    
    # get the strategies for the specifc driver
    driver_data = df[df["Driver"] == selected_driver]
    for year, group in driver_data.groupby("Year"):
        group = group.sort_values(by='Stint')
        compound_list = group['Compound'].tolist()
        pitlap_list = group['PitLap'].tolist()
        length_list = group['StintLength'].tolist()
        
        # append the stints
        if compound_list:
            strategy = list(zip(compound_list, pitlap_list, length_list))
            strategies.append(strategy)

if not strategies:
    print("No strategies found for given input.")
    exit(1)


# count most common strategy
strategy_counts = Counter(tuple(s) for s in strategies)
most_common = strategy_counts.most_common(1)[0][0]

# output result
print("\nFull strategy breakdown:")
for i, (compound, pitlap, stint_len) in enumerate(most_common):
    # replace pit lap with FIN if last lap 
    pitlap_display = "END" if int(pitlap) in LAPS else int(pitlap)
    print(f"Stint {i + 1}: {compound}, pit lap = {pitlap_display}, stint length = {int(stint_len)}")
print(f"time loss in pitlane (avg) = {TIME_LOSS}s\ntotal time loss with this strat = {TIME_LOSS * len(most_common)}s")
print(f"time loss in pitlane under saftey car(avg) = {TIME_LOSS_SC}s\ntotal time loss with this strat with saftey car= {TIME_LOSS_SC * len(most_common)}s")
