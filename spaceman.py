
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

word = "astronaut"

# getting user input
def user_input(prompt):
    user_input = input(prompt)
    return user_input


# def game_start():
