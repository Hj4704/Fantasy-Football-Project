from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    stats_url = "https://api.sleeper.app/v1/stats/nfl/regular/2025/17"
    players_url = "https://api.sleeper.app/v1/players/nfl"

    try:
        stats_response = requests.get(stats_url)
        players_response = requests.get(players_url)

        stats_data = stats_response.json()
        players_data = players_response.json()
    except Exception as e:
        return f"Error fetching data: {e}"

    if not isinstance(stats_data, dict):
        return "Unexpected data format from Sleeper API."

    players = []

    # stats_data = {player_id: {stat_dict}}
    for player_id, stat in stats_data.items():
        points = stat.get("pts_ppr", 0)

        if player_id in players_data:
            player = players_data[player_id]
            name = player.get("full_name", "Unknown")
            team = player.get("team", "FA")
            pos = player.get("position", "N/A")

            players.append({
                "name": name,
                "team": team,
                "position": pos,
                "points": round(points, 2)
            })

    players = sorted(players, key=lambda x: x["points"], reverse=True)

    return render_template("index.html", players=players[:25])

if __name__ == '__main__':
    app.run(debug=True, port=5001)