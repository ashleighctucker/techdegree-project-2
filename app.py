import constants


def clean_data():
    clean_players = [player for player in constants.PLAYERS]

    for player in clean_players:

        #convert guardian string to listr
        player['guardians'] = player['guardians'].split(" and ")

        #convert height to int
        player['height'] = player['height'].split(" ")
        player['height'] = int(player['height'][0])

        #convert experience to bool
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False

        print(player['guardians'])

    return clean_players


def balance_teams:
    

lean_players = clean_data()
