# Games Store/Plan Abrutly Goblins game night (abruptly_goblins.py)
# Create a system for organizing and tracking gamer’s availability.

# Empty list to store the people who are attending game night
gamers = []

# Gamers
kimberly = {'name': 'Kimberly Warner', 
           'availability': ["Monday", "Tuesday", "Friday"]}
thomas = {'name': 'Thomas Nelson', 
           'availability': ["Tuesday", "Thursday", "Saturday"]}
joyce = {'name': 'Joyce Sellers', 
           'availability': ["Monday", "Wednesday", "Friday", "Saturday"]}
michelle = {'name': 'Michelle Reyes', 
           'availability': ["Wednesday", "Thursday", "Sunday"]}
stephen = {'name': 'Stephen Adams', 
           'availability': ["Thursday", "Saturday"]}
joanne = {'name': 'Joanne Lynn', 
           'availability': ["Monday", "Thursday"]}
latasha = {'name': 'Latasha Bryan', 
           'availability': ["Monday", "Sunday"]}
crystal = {'name': 'Crystal Brewer', 
           'availability': ["Thursday", "Friday", "Saturday"]}
james = {'name': 'James Barnes Jr.', 
           'availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}
michel = {'name': 'Michel Trujillo', 
           'availability': ["Monday", "Tuesday", "Wednesday"]}
francis = {'name': 'Francis Monk'}

# List of gamers names
players_name = [kimberly, thomas, joyce, michelle, stephen, joanne, latasha,
                crystal, james, michel, francis]

# Define function to add gamers to the gamers list
def add_gamer(gamer, gamers_list):
    if gamer.get('name') and gamer.get('availability'):
        gamers_list.append(gamer)
    else:
        print(f'Missing required information for: {gamer}, ' 
              f'index: {players_name.index(gamer)} of players_name list.\n')

# Add gamers to the list
for name in players_name:
    add_gamer(name, gamers)
print(f'Current Players:\n{gamers}\n')

# Define function to create a weekly calendar
def build_daily_frequency_table(gamers_list=gamers):
    lst = []
    days_dictionary = {}
    for gamer in gamers_list:
        lst.append(gamer.get('availability'))
    for days in lst:
        for day in days:
            days_dictionary[day] = 0    
    return days_dictionary

count_availability = build_daily_frequency_table()

# Define function to calculate daily availability for each gamer
def calc_availability(gamers_list=gamers, available_frequency=count_availability):
    for gamer in gamers_list:
        for day in gamer['availability']:
            available_frequency[day] += 1

calc_availability()

# Sort the availability in descending order
count_availability_sorted = {key: value for key, value 
in sorted(count_availability.items(), key=lambda value: value[1], reverse=True)}
print(f'Gamers Availability:\n{count_availability_sorted}\n')

# Define function to find best day to host game night
def find_best_night(availability_table=count_availability_sorted):
    count = 0
    for day in availability_table:
        if availability_table[day] > count:
            count = availability_table[day]
        if availability_table[day] == count:
            best_night = day
    return best_night

game_night = find_best_night()
print(f'Best day to host game night: {game_night}\n')

# Define function to find the people available for game night
def available_on_night(gamers_list=gamers, day=game_night):
    gamers_available = []
    for gamer in gamers_list:
        if day in gamer['availability']:
            gamers_available.append(gamer)
    return gamers_available

attending_game = available_on_night()
print(f'People attending game night:\n{attending_game}\n')

# Write the invitation email
form_email = '''
Hey there {name}!

Hope this message finds you ready fellow adventurer\
 because something magical is brewing at Sorcery Society! 🧙‍♂️✨

We're thrilled to announce that our next adventure\
 in the mystical realm of Abruptly Goblins awaits! 

Prepare your dice, sharpen your wits, and don your most enchanted gear,\
 for on {day_of_week} of next week that's when the real adventure begins! 
Get ready to roll the dice, cast some spells,\
 and perhaps even slay a goblin or two. 🦾💥

We can't wait to see you there, {name}!\
 Bring your friends, bring your spirit,\
 and let's make this game night one for the history books.

May your rolls be lucky and your quests be legendary!

Best magical regards,
Your friends at the Sorcery Society 🧙‍♀️🔮
'''

# Send the invitation email
def send_email(attending_gamers=attending_game, day=game_night):
    for gamer in attending_gamers:
        print(form_email.format(name=gamer['name'], day_of_week=day))

send_email()

# Create a list for the  gamers unable to attend game night
unable_to_attend_best_night = [gamer for gamer in gamers\
                                if game_night not in gamer['availability']]

# Create second night weekly calendar
second_night_availability = \
    build_daily_frequency_table(gamers_list=unable_to_attend_best_night)

# Calculate daily availability for gamers unable to attend best night
calc_availability(gamers_list=unable_to_attend_best_night,\
                  available_frequency=second_night_availability)

# Sort the second night availability in descending order
second_night_availability_sorted = {key: value for key, value 
in sorted(second_night_availability.items(), key=lambda value: value[1], reverse=True)}
print(f'Gamers availability for the second night:\n{second_night_availability_sorted}\n')

# Find best day to host the second game night
second_night = find_best_night(availability_table=second_night_availability_sorted)
print(f'Best day to host second game night: {second_night}\n')

# Find out who are the people available for the second game night
# (whether they can attend the first night or not)
available_second_game_night = available_on_night(gamers_list=gamers, day=second_night)
print(f'People attending second game night:\n{available_second_game_night}\n')

# Send the second invitation email
send_email(attending_gamers=available_second_game_night, day=second_night)
