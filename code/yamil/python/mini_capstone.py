import requests
import pprint
import json

# Sport Codes:
# NCAA Football
# NFL
# MLB
# NBA
# NCAA Men's Basketball
# NHL
# UFC MMA
# WNBA
# MLS
# EPL
# FRA1
# GER1
# ESP1
# ITA1
# UEFACHAMP
# FIFA

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

# for i in data['events'][i]['teams_normalized']:
for i in range(len(data['events'])):
    match = []
    for teams in data['events'][i]['teams_normalized']:
        # match.append(teams['abbreviation'])
        match.append(teams['abbreviation']+" "+teams['name'])
    matches.append(match)
print(matches)