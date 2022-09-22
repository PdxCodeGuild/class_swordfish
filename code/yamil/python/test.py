players_csv_outcome = [
{"name" : "cristiano ronaldo", "current club" : "manchester united", "european league" : "premier league"},
{"name" : "lionel messi", "current club" : "paris st germaine", "european league" : "ligue 1"},
{"name" : "radamel falcao", "current club" : "rayo vallecano", "european league" : "la liga"}
]


for x in range(len(players_csv_outcome)):
    players_csv_outcome_print = "".join(str(players_csv_outcome[x]))


print(players_csv_outcome_print)