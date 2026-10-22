from flask import Flask, render_template
from datetime import datetime
import random

app = Flask(__name__)


@app.route('/')
def home():
    now = datetime.now()
    current_year = now.year
    current_day = now.day
    current_now = now
    current_month = now.strftime("%B")
    return render_template("index.html", now=current_now, year=current_year, month=current_month, day=current_day)


@app.route('/card')
def card():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    randomRank = random.choice(ranks)
    randomSuit = random.choice(suits)
    return render_template("card.html", rank=randomRank, suit=randomSuit)

@app.route('/season-facts')
def season_facts():
    facts = {
        "Winter": "Minnesota's coldest recorded temperature is -60°F.",
        "Spring": "The spring equinox gives nearly equal day and night.",
        "Summer": "The summer solstice is the longest day of the year.",
        "Fall": "Leaves change color as chlorophyll breaks down.",
    }
    return render_template("season_facts.html", facts=facts)


@app.route('/activities')
def activities():
    season = "Winter"
    things_to_do = ["Ice fishing", "Skating", "Snowshoeing", "Hot cocoa"]
    return render_template("activities.html", season=season, things_to_do=things_to_do)