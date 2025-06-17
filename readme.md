# General strategy prediction based on Zandvoort F1 data
A command-line tool that predicts the most common F1 race strategy at Zandvoort based on historical tyre data from 2021–2024. Given a starting compound, it outputs a stint-by-stint breakdown with pit laps, stint lengths, and estimated time loss in the pit lane.

## Features
- Predicts most common race strategies based on real-world data
- Outputs compound per stint, pit lap, and stint length
- Includes time loss estimates for both normal pit stops and safety car conditions
- Clean and simple CLI interface — no unnecessary dependencies

## Example Usage
```
$ python3 predictor.py --compound MEDIUM

Full strategy breakdown:
Stint 1: MEDIUM, pit lap = 30, stint length = 30
Stint 2: HARD, pit lap = END, stint length = 41

time loss in pitlane (avg) = 22s
total time loss with this strat = 44s
time loss in pitlane under saftey car(avg) = 17s
total time loss with this strat with saftey car= 34s
```

## Setup
1) Clone this repo
```
git clone https://github.com/mjwakex/zandvoort-strategy-predictor.git
cd zandvoort-strategy-predictor
```
2) Create a virtual environment
```
python3 -m venv venv
source venv/bin/activate
```
3) Install dependencies
``` 
pip install -r requirements.txt 
```
4) Run the predictor
``` 
python3 src/predictor.py --compound HARD 
```

## Data
The model uses historical stint and tyre compound data from the Dutch Grand Prix (Zandvoort) between 2021–2024. Data was sourced using FastF1 (https://docs.fastf1.dev/index.html) and manually curated.

## Future Plan
Building a machine learning model to predict optimal strategies based on race conditions, and add support for driver specific strategy analysis.

## Author
Made by Marcus Elizondo-Darwin — passionate about racing strategy, data analysis, and F1.
If you liked this, feel free to connect on LinkedIn (https://www.linkedin.com/in/marcus-elizondo-darwin/).
