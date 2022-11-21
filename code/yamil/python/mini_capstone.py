from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
import requests
import pprint
import json

print("\n""Welcome to Yamil's Bets!""\n")

sport_codes = {
    "NCAA" : 1,
    "NFL" : 2,
    "MLB" : 3,
    "NBA" : 4,
    "NCAA" : 5,
    "NHL" : 6,
    "UFC" : 7,
    "WNBA": 8,
    "CFL" : 9,
    "MLS": 10,
    "EPL": 11,
    "FRA1": 12,
    "GER1": 13,
    "ESP1": 14,
    "ITA1": 15,
    "UEFACHAMP": 16,
    "FIFA": 17
}
choose_sport = input("What sport would you like to see?: ")
choose_date = input("What date would you like to see?: ")
url = f"https://therundown-therundown-v1.p.rapidapi.com/sports/{sport_codes[choose_sport]}/events/{choose_date}"

querystring = {"include":"scores","offset":"0"}

headers = {
	"X-RapidAPI-Key": "93f2bf0191mshc55c842a845a8c7p1c2c0fjsndd414bd6673f",
	"X-RapidAPI-Host": "therundown-therundown-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()

matches = []
match = []

for i in range(len(data['events'])):
    match = []
    for teams in data['events'][i]['teams_normalized']:    
        if choose_sport in ['NFL', "MLS","MLB","NBA"]:
            match.append(teams['name']+" "+teams['mascot'])
        else:
            match.append(teams['name'])
    matches.append(match)

print(f"{matches[0][0]} odds are: {data['events'][0]['lines']['11']['moneyline']['moneyline_away']}")
print(f"{matches[0][1]} odds are: {data['events'][0]['lines']['11']['moneyline']['moneyline_home']}")

away_odds = data['events'][0]['lines']['11']['moneyline']['moneyline_away']
home_odds = data['events'][0]['lines']['11']['moneyline']['moneyline_home']

winner = ""
if home_odds < away_odds:
    winner = f"{matches[0][1]}"
else:
    winner = f"{matches[0][0]}"

def demo(screen):
    effects = [
        Cycle(
            screen,
            FigletText("BET", font='small'),
            int(screen.height / 2 - 5)),
        Cycle(
            screen,
            FigletText("ON", font='small'),
            int(screen.height / 2 - .5)),
        Cycle(
            screen,
            FigletText(f"{winner}", font='small'),
            int(screen.height / 2 + 3)),
    ]
    screen.play([Scene(effects, 500)])

Screen.wrapper(demo)