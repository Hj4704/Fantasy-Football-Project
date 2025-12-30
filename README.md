# Fantasy Football Top Scorers (Flask Web App)

A Flask web app that pulls live NFL week stats from the Sleeper API and displays the current Top 25 fantasy scorers (PPR) in a table.
Currently working on updating the table and adding predictive features for player stats and scores.

# Demo

Not hosted yet. Run locally using the steps below.

# Features

- Displays Top 25 players** by PPR fantasy points** for the current NFL week**
- Automatically detects the current season / season type / week using Sleeper’s state/nfl endpoint
- Shows player data (name, team, position) by joining stats with the Sleeper player directory
- Simple server-rendered UI using Jinja templates
- Player directory caching to reduce load time

# Tech Stack

- Backend: Python, Flask
- Data/API: Sleeper API
- Frontend: HTML/CSS + Jinja templates

# Getting Started (Run Locally)
1. Install Python 3.9+
2. Clone the repo: git clone https://github.com/Hj4704/Fantasy-Football-Project.git
3. cd Fantasy-Football-Project
4. python3 -m venv .venv
5. source .venv/bin/activate
6. pip install -r requirements.txt
7. python main.py
8. Open in browser go to: http://127.0.0.1:5001/


