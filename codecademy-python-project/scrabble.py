# Scrabble (scrabble.py)
# Use Python dictionary to keep point totals for people playing scrabble.

import random
import nltk

# Download the 'words' corpus from NLTK
nltk.download('words')

from nltk.corpus import words

# List of letters
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
            "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# List of points per letter
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3,
           10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Merge the two lists into a dictionary
scrabble_dict = {key: value for key, value in zip(letters, points)}
print(f'Scrabble Dictionary:\n{scrabble_dict}\n')

# Add blank tiles to the dictionary
scrabble_dict[' '] = 0
print(f'Scrabble Dictionary with Blank Tile:\n{scrabble_dict}\n')

# Define function to find how many points a randomly selected word is worth
def score_word(word=random.choice(words.words())):
  points = 0
  for i in word.upper():
    points += scrabble_dict.get(i)
  return word, points

random_word, total_points = score_word()
print(f'Random Generation:\n'
      f'Word Played: {random_word.title()}\nPoints: {total_points}\n')

# Create new dictionary that maps players to a list of their played words
players_words = {'Gamer1': ['BLUE', 'TENNIS', 'EXIT'], 
                 'WordNerd': ['EARTH', 'EYES', 'MACHINE'],
                 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 
                 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}

# Define a function that creates a dictionary of the words played by each player +
# the respective point value.
def word_played():
  played_words = {}
  for player, words in players_words.items():
    played_words[player] = []
    for word in words:
      played_words[player].append(f'Word played No.{words.index(word) + 1}: {word}. '
                          f'Points: {score_word(word)[1]}')
  return played_words

print(f'Players Word and Points Dictionary:\n{word_played()} \n')

# Create a new dictionary that maps each player with the total sum of points obtained.
players_total_points = {}

for player, words_played in players_words.items():
  points = 0
  for word in words_played:
    points += score_word(word)[1]
  players_total_points[player] = points
print(f'Players\' Total Score: {players_total_points}\n')

# Declare the winner
winner = None
for player, points in players_total_points.items():
    if winner is None or points > players_total_points[winner]:
       winner = player
print(f'Winner: {winner}')
