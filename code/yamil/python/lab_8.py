import re
from threading import local

def c(header, local_list):
    name_add = input("Please enter the player's name: ")
    club_add = input("Please enter the player's team: ")
    league_add = input("Please enter the player's league: ")

    player_dict = {
        header[0] : name_add,
        header[1] : club_add,
        header[2] : league_add
    }

    local_list.append(player_dict)
    print(local_list)
    return local_list

def r(local_list_2):
    retrieve = input("Which player would you like to see?: ")
    for i in range(len(local_list_2)):
        if local_list_2[i]['name'].lower() == retrieve.lower():
            return local_list_2[i]

def u(local_awesome_player_list):
    update = input("Which player would you like to update?: ")
    for i in range(len(local_awesome_player_list)):
        if local_awesome_player_list[i]['name'].lower() == update.lower():
            update_question = input("What attribute would you like to update?: Club or League? ")
            if update_question.lower() == "club":
                update_attribute_club = input("Please enter the new club: ")
                local_awesome_player_list[i]["club"] = update_attribute_club.lower()
            elif update_question.lower() == "league":
                update_attribute_league = input("Please enter the new league: ")
                local_awesome_player_list[i]["league"] = update_attribute_league.lower()
            else:
                print("Please enter either club or league.")
    print(local_awesome_player_list)
    return local_awesome_player_list

def d(local_list_3):
    delete = input("Which player would you like to delete?: ")
    for i in range(len(local_list_3)-1, -1, -1):
        if local_list_3[i]['name'].lower() == delete.lower():
            del local_list_3[i]
    return local_list_3

# --------------------------------------------------------------------------------------------

with open("csv_copy.csv", "r") as f:
    csv = f.read()

lines = csv.split("\n")
header_2 = lines[0]
header = lines[0].split(",")

player_list = []
awesome_player_list = []
new_line = "\n"
choices = ["end", "create", "retrieve", "update", "delete", "options"]


for i in range(1,len(lines)):
    player = lines[i].split(",")
    player_list.append(player)

for i in range(len(player_list)):
    awesome_player_list.append(dict(zip(header, player_list[i])))
    

player_csv_print = []

while True:
    crud_choice = input("What would you like to do? Please enter 'options' if you need assistance. \n")
    if crud_choice.lower() == "options":
        print(f"Your options are: {choices}.")
    elif crud_choice.lower() == "create":
        awesome_player_list = c(header, awesome_player_list)
    elif crud_choice.lower() == "retrieve":
        awesome_player = r(awesome_player_list)
        if awesome_player:
            print(awesome_player)
        else:
            print("Player is not currently active.")
    elif crud_choice.lower() == "update":
        awesome_player_list = u(awesome_player_list)
    elif crud_choice.lower() == "delete":
        awesome_player_list = d(awesome_player_list)
    elif crud_choice.lower() == "end":
        print(awesome_player_list)
        for i, x in enumerate(awesome_player_list):
            player_csv_print.append(f"{x['name']},{x['club']},{x['league']}")
            player_csv_print_2 = "\n".join(str(e) for e in player_csv_print)
            player_csv_print_2 = header_2 + new_line + player_csv_print_2
        with open("csv_copy.csv", "w") as f2:
            f2.write(player_csv_print_2)
        break
    else:
        print("Please enter a valid option.")




# players_csv_outcome = [
# {"name" : "cristiano ronaldo", "current club" : "manchester united", "european league" : "premier league"},
# {"name" : "lionel messi", "current club" : "paris st germaine", "european league" : "ligue 1"},
# {"name" : "radamel falcao", "current club" : "rayo vallecano", "european league" : "la liga"}
# ]