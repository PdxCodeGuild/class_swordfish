import re

# players_csv_outcome = [
# {"name" : "cristiano ronaldo", "current club" : "manchester united", "european league" : "premier league"},
# {"name" : "lionel messi", "current club" : "paris st germaine", "european league" : "ligue 1"},
# {"name" : "radamel falcao", "current club" : "rayo vallecano", "european league" : "la liga"}
# ]

with open("csv_copy.csv", "r") as f:
    csv = f.read()

lines = csv.split("\n")
header_2 = lines[0]
header = lines[0].split(",")

player_list = []
player_csv = []
new_line = "\n"
choices = ["end", "create", "retrieve", "update", "delete", "options"]


for i in range(1,len(lines)):
    player = lines[i].split(",")
    player_list.append(player)

for i in range(len(player_list)):
    player_csv.append(dict(zip(header, player_list[i])))
    

def c():
    added_info = []
    name_add = input("Please enter the player's name: ")
    added_info.append(name_add.lower())
    team_add = input("Please enter the player's team: ")
    added_info.append(team_add.lower())
    league_add = input("Please enter the player's league: ")
    added_info.append(league_add.lower())
    player_csv.append(added_info)
    return player_csv



def r():
    retrieve = input("Which player would you like to see?: ")
    for i in range(len(player_csv)):
        if player_csv[i]['name'].lower() == retrieve.lower():
            print(player_csv[i])
            return(player_csv[i])
    if player_csv[i]['name'] != retrieve:
        print("Player is not currently active.")
        return player_csv

def u():
    update = input("Which player would you like to update?: ")
    for i in range(len(player_csv)):
        if player_csv[i]['name'].lower() == update.lower():
            update_question = input("What attribute would you like to update?: Club or League? ")
            if update_question.lower() == "club":
                update_attribute_club = input("Please enter the new club: ")
                player_csv[i]["club"] = update_attribute_club.lower()
            elif update_question.lower() == "league":
                update_attribute_league = input("Please enter the new league: ")
                player_csv[i]["league"] = update_attribute_league.lower()
            else:
                print("Please enter either club or league.")
    return player_csv

def d():
    delete = input("Which player would you like to delete?: ")
    for i in range(len(player_csv)-1, -1, -1):
        if player_csv[i]['name'].lower() == delete.lower():
            del player_csv[i]
    return player_csv

player_csv_print = []

while True:
    crud_choice = input("What would you like to do?:  ")
    if crud_choice.lower() == "options":
        print(f"Your options are: {choices}.")
    elif crud_choice.lower() == "create":
        c()
    elif crud_choice.lower() == "retrieve":
        r()
    elif crud_choice.lower() == "update":
        u()
    elif crud_choice.lower() == "delete":
        d()
    elif crud_choice.lower() == "end":
        for i, x in enumerate(player_csv):
            player_csv_print.append(f"{x['name']},{x['club']},{x['league']}")
            player_csv_print_2 = "\n".join(str(e) for e in player_csv_print)
            player_csv_print_2 = header_2 + new_line + player_csv_print_2
        with open("csv_copy.csv", "w") as f2:
            f2.write(f"{player_csv_print_2}")
        break
    else:
        print("Please enter a valid option.")