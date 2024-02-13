# Import random module
import random

# Declare variable to store randomly generated number
random_number = random.randint(1, 12)

# Add empty line for readability
print('\n')

# print the greetings
print('Welcome to the Magic 8 Ball Game \n')

# Provide examples of suitable questions
print('''Ask a yes/no question about yourself or your dreams.
Then, wait for the 8 Ball to work its magic. \n''')

# Initialize player_name and player_question as empty strings
player_name = ''
player_question = ''

# Prompt player for name and question
while player_name == '':
    player_name = input('What\'s your name? ')
    if player_name == '':
       print('Please, provide a name.')

while player_question == '':
    player_question = input('What\'s your question? ')
    if player_question == '':
        print('Please, provide a question.')

# Print player's name, question and ask the player to wait
print('\n' + player_name + '\'s question:', player_question)
print('Channeling my power, please wait...')

# Declare variable that stores 8-ball answer
answer = ''

# if statement to assign answers to the random generated value
if random_number == 1:
   answer = 'Yes - definitely'
elif random_number == 2:
   answer = 'It is decidedly so'
elif random_number == 3:
   answer = 'Most likely!'
elif random_number == 4:
   answer = 'Without a doubt'
elif random_number == 5:
   answer = 'Reply hazy, try again'
elif random_number == 6:
   answer = 'Ask again later'
elif random_number == 7:
   answer = 'Better not tell you now'
elif random_number == 8:
   answer = 'Ask someone else.'
elif random_number == 9:
   answer = 'My sources say no'
elif random_number == 10:
   answer = 'Outlook not so good'
elif random_number == 11:
   answer = 'Very doubtful'
elif random_number == 12:
   answer = 'Don\'t count on it'

# Print 8-ball answer
print('\n🔮 The mystic 8-ball speaks:', answer)

# Add empty line for readability
print('\n')