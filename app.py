import constants
import copy


def clean_guardians(player_list):
    for player in player_list:
        player['guardians'] = player['guardians'].split(" and ")


def clean_height(player_list):
    for player in player_list:
        player['height'] = int(player['height'].split(" ")[0])


def clean_experience(player_list):
    for player in player_list:
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False


def clean_data():
    clean_players = copy.deepcopy(constants.PLAYERS)
    clean_guardians(clean_players)
    clean_height(clean_players)
    clean_experience(clean_players)
    return clean_players


def sort_by_experience(player_list):
    experienced_players = []
    inexperienced_players = []
    for player in player_list:
        if player['experience'] == True:
            experienced_players.append(player)
        else:
            inexperienced_players.append(player)
    return experienced_players, inexperienced_players


def balance_teams(player_list_1, player_list_2):
    teams_copy = copy.deepcopy(constants.TEAMS)
    teams_copy[0] = player_list_1[0:3] + player_list_2[0:3]
    teams_copy[1] = player_list_1[3:6] + player_list_2[3:6]
    teams_copy[2] = player_list_1[6:9] + player_list_2[6:9]
    return teams_copy


def count_experience(team):
    count = []
    for player in team:
        if player['experience'] == True:
            count.append(player)
    return len(count)


def average_height(team):
    height = 0
    for player in team:
        height += player['height']
    average_height = round(float(height / len(team)),2)
    return average_height


def create_player_list(team):
    player_list = []
    for player in team:
        player_list.append(player['name'])
    return ", ".join(player_list)


def create_guardian_list(team):
    guardian_list = []
    for player in team:
        guardian_list += player['guardians']
    return ", ".join(guardian_list)


def display_team(team_name, team):

    print("\nTeam:  {} Stats".format(team_name))
    print("---------------------\n")
    print("Total Players:  {}\n".format(len(team)))
    print("Total Experienced:  {}\n".format(count_experience(team)))
    print("Total Inexperienced:  {}\n".format(len(team) - count_experience(team)))
    print("Average Height: {}\n".format(average_height(team)))
    print("Players on Team:\n{}\n".format(create_player_list(team)))
    print("Guardians:\n{}\n\n".format(create_guardian_list(team)))
    print("---------------------\n")

def pick_team(teams_list):
    while True:
        print("1)  Panthers")
        print("2)  Bandits")
        print("3)  Warriors")
        try:
            choice = int(raw_input("\nEnter a team option:   "))
            if choice < 1:
                raise ValueError()
            if choice > 3:
                raise ValueError()
        except ValueError:
            print("Sorry, that's an invalid input. Please select 1, 2, or 3.")
        else:
                if choice == 1:
                    display_team("Panthers", teams_list[0])
                    break
                elif choice == 2:
                    display_team("Bandits", teams_list[1])
                    break
                elif choice == 3:
                    display_team("Warriors", teams_list[2])
                    break


def start_tool():

    while True:
        print("Here are your choices:\n \n1)  Display Team Stats\n2)  Quit\n")
        try:
            option = int(raw_input("Enter an option:   "))
            if option < 1:
                raise ValueError()
            if option > 2:
                raise ValueError()
        except ValueError:
            print("Sorry, that's not a valid input. Please select 1 or 2.")
        else:
            if option == 2:
                print("Closing Stats Tool...")
                break
            elif option == 1:
                pick_team(balanced_teams)
                continue

if __name__ == "__main__":
    print("---------------------\nBasketball Stats Tool\n---------------------")
    clean_players = clean_data()
    experienced_players, inexperienced_players = sort_by_experience(clean_players)
    balanced_teams = balance_teams(experienced_players, inexperienced_players)
    start_tool()
