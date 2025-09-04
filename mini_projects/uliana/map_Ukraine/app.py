from flask import Flask, render_template
import csv
import os

app = Flask(__name__)

def load_points():
    coordinates = []
    path = os.path.join("static", "coordinates.csv")
    with open(path, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            coordinates.append({
                "x": int(row["x"]),
                "y": int(row["y"]),
                "oblast": row["oblast"]
            })
    return coordinates

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/start")
def start():
    return render_template("start.html")

@app.route("/game")
def start_game():
    coordinates = load_points()
    return render_template("game.html", coordinates=coordinates)

@app.route("/learning")
def start_learn():
    coordinates = load_points()
    return render_template("learn.html", coordinates=coordinates)

if __name__ == '__main__':
    app.run()
