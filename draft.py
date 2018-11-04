import random

def intro_screen():
  name = input("gimme ur name>> ")
  print("Welcome to Spaceman, " + name + "!")
  print("###################################")
  print("You have 6 lives in this game. Start guessing")
  hangman()
  print()

def hangman():
  word = random.choice(["wonderland", "aquarium", "croatia"])
  turns = 10
  guessed = " "


  while len(word) > 0:
    msg = ""
    missed = 0

    for letter in word:
      if letter in guessed:
        msg = msg+letter
      else:
        msg = msg + "_" + " "
        missed += 1

    if msg == word:
      print(msg)
      print("correct! word is " + word)
      break

    print("Guess the word: " + msg)
    guess = input()

    if guess.isalpha():
      guessed = guessed + guess
    else:
      print("enter valid letter: ")
      guess = input()
    
    if guess not in word:
      turns = turns - 1
      if turns == 9:
        print(" o")
      if turns == 8:
        print(" o")
      if turns == 7:
        print(" o")
      if turns == 6:
        print(" o")
      if turns == 5:
        print(" o")
      if turns == 4:
        print(" o")
      if turns == 3:
        print(" o")
      if turns == 2:
        print(" o")
      if turns == 1:
        print("LOST!" + word)
        break

intro_screen()


# +++++++++++++++++++++++++++++=============

# answerlist = ["wonderland", "aquarium", "croatia"]
# random.shuffle(answerlist)

# answer = list(answerlist[0])

# display = []
# display.extend(answer)

# for i in range(len(display)):
#   display[i] = "_"

# print(" ".join(display))
# print()

# count = 0

# while count < len(answer):
#   guess = input("guess a letter: ")
#   guess = guess.lower()
#   print(count)

#   for i in range(len(answer)):
#     if answer[i] == guess:
#       display[i] = guess
#       count = count + 1

#   print(" ".join(display))
#   print()

# print("you won!")


import random
# ============== RULES/REQS ================

# show blanks _ _ _ _ _ _ _
# exchange blanks with correct guesses
# max of 7 wrong guesses
# previously wrong guesses are not count >> print notification
# display: wrongly guessed letters
# display: number of guesses(life) left
# after 7 wrong guesses game over
# if the word is guessed player wins

# ============== PSEUDOCODE for MVP================

# start with printing "started" and show "you have 7 chances" word is "astronaut"
# display blanks
# ask guess
# show if its wrong or right
# if wrong -1 from 7 chances show array of wrong letters
# if correct display the letter

# ============== functions ================
# game_start >> start the game
# check >> compares user input with correct letter array
# exchange >> exchange blank with correct answer
# wrong_answer >> appends wrong letters array and displays it
# right_answer >> appends right letters array
# display >> displays wrong answer array
# count >> counts 7 lives
# user input >> gets user input

# getting user input
# def user_input(prompt):
#     user_input = input(prompt)
#     return user_input


# # words_list = ["wonderland", "aquarium", "croatia"]
# # secret_word = random.shuffle(words_list)
# secret_word = "spaceman"
# wrong_guesses = []
# space_mark = " _ "


# missed_chances = 0
# chances = 7

# def guessing():
#     missed_chances = 0
#     # printing underscore
#     print(space_mark * len(secret_word))
#     # asking input
#     letter = user_input("gimme letter>> ")
#     if letter in secret_word:
#         print("yes")
#     else:
#         print("no")
#         missed_chances +=1
#         wrong_guesses.append(letter)
#         print(wrong_guesses)
#     return letter


# def game_goes_on():
#     while chances > missed_chances:
#         guessing()
#     else:
#         print("lost")
#         exit()

# def spaceman():
#     guessing()
#     game_goes_on()

# spaceman()


# MVP
""" 
1. program counts missed chances
2. program displays _ _ _ _ _ _
3. program stops when missed chances > chances

"""

""" 
Error handling
Try except block except >> catches error
Wrong type of character (isDigit, ischar is in alphabet) >> should be only character
Check if the input is one letter >> 
Repeated input
"""
