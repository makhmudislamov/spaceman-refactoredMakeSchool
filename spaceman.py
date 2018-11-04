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
SPACEMAN = (
"""
1st
""",
"""
2nd
""",
"""
3rd
"""

)

print(SPACEMAN[0])
play_again = True
while play_again:

    words_list = ['netherland', 'croatia', 'angelina']
    chosen_word = random.choice(words_list).lower()
    guess = None
    # contains guessed letters
    guessed_letters = []
    blank_word = []

    for letter in chosen_word:
        blank_word.append('_')
    attempts = 6

    if attempts != 0 and '_' in blank_word:
        print(('\nYou have {} attempts left').format(attempts))
    try:
        guess = str(input('\Please select a letter between A-Z')).lower()
    except:
        print('That is not valid input. Please try again.')
        continue
    
    else:
        if not guess.isalpha():
            print('Your input was not a letter. Please try again.')
            continue
        elif len(guess) > 1:
            print('That is more than one letter. Please try again.')
            continue
        elif guess in guessed_letters:
            print('You made this input earlier. Please try again.')
