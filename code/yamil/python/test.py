players_csv_outcome = [
{"name" : "cristiano ronaldo", "club" : "manchester united", "league" : "premier league"},
{"name" : "lionel messi", "club" : "paris st germaine", "league" : "ligue 1"},
{"name" : "radamel falcao", "club" : "rayo vallecano", "league" : "la liga"}
]
headers = ["name, "]

# for x in range(len(players_csv_outcome)):
#     players_csv_outcome_print = "\n".join(players_csv_outcome)


# for i in players_csv_outcome:
#     print(f"{i['name']},{i['club']}, {i['league']}")

# "\n".join(players_csv_outcome)
players_csv_outcome_print = []
for i, x in enumerate(players_csv_outcome):
    players_csv_outcome_print.append(f"{x['name']},{x['club']},{x['league']}")

"\n".join(players_csv_outcome_print)
print(players_csv_outcome_print)