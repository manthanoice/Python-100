import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
words = ['apple', 'banana', 'america', 'nice', 'helikopter']
chosen_word = random.choice(words)
# print("Chosen word is {}".format(chosen_word))
word_length = len(chosen_word)

the_list = []
for i in range(0, word_length):
    the_list.append("_")
print(" ".join(the_list))

list_length = len(stages)-1
print(stages[list_length])

while the_list.count("_") != 0:
    guess_letter = input("Enter your guess letter here: ").lower()
    for i in range(0, word_length):
        letter = chosen_word[i]
        if letter == guess_letter:
            the_list[i] = letter
    if guess_letter not in chosen_word:
        list_length-=1
    print(stages[list_length])
    print(" ".join(the_list))
    if list_length==0:
        print("You lost!")

if(the_list.count("_")==0):
    print("You won!")