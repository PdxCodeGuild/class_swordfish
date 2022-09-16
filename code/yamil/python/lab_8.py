import re

players_list_outcome = [
{"name" : "cristiano ronaldo", "current club" : "manchester united", "european league" : "premier league"},
{"name" : "lionel messi", "current club" : "paris st germaine", "european league" : "ligue 1"},
{"name" : "radamel falcao", "current club" : "rayo vallecano", "european league" : "la liga"}
]

with open("csv_copy.csv", "r") as f:
    csv = f.read()

csv_lines = csv.split("\n")
tabs = csv_lines[0].split(",")
# cr7 = full_list[1].split(",")
# m10 = full_list[2].split(",")
# km7 = full_list[3].split(",")

player_list = []
player_dict = {}

for i in range(1,len(csv_lines)):
    player = csv_lines[i].split(",")
    player_list.append(player)


# for i in range(full_list):