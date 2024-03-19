import csv
import json

# List of users whose passwords have been compromised
compromised_users = []

# Open and Read passwords.csv
with open('passwords.csv', newline='') as password_file:
  password_csv = csv.DictReader(password_file)
  for line in password_csv:
    password_row = line
    compromised_users.append(password_row['Username'])

print(f'List of all the compromised users:\n{compromised_users}')

# Open a new file, compromised_users.txt
with open('compromised_users.txt', 'w') as compromised_user_file:
  for user in compromised_users:
    compromised_user_file.write(f'\n{user}')

# Create a json file
with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {'recipient': 'The Boss', 'message': 'Mission Success'}
  json.dump(boss_message_dict, boss_message)

# Remove passwords.csv
with open('new_passwords.csv', 'w') as new_passwords_obj:
  slash_null_sig = '''
_  _     ___   __  ____             
/ )( \\   / __) /  \\(_  _)            
) \\/ (  ( (_ \\(  O ) )(              
\\____/   \\___/ \\__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \\ / _\\  / __)(  / )(  __)(    \\ 
) __ (/    \\( (__  )  (  ) _)  ) D ( 
\\_)(_/\\_/\\_/ \\___)(__\\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\\ / ___)/ )( \\
(___)  \\___ \\/ (_/\\/    \\\\___ \\) __ (
       (____/\\____/\\_/\\_/(____/\\_)(_/
 __ _  _  _  __    __                
(  ( \\/ )( \\(  )  (  )               
/    /) \\/ (/ (_/\\/ (_/\\           
\\_)__)\\____/\\____/\\____/
'''
  new_passwords_obj.write(slash_null_sig)

