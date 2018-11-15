import random

SPACEMAN = [
"""
1stanimation
""",
"""
2ndanimation
""",
"""
3rdanimation
""",
"""
4thanimation
""",
"""
5thanimation
""",
"""
6thanimation  
"""
]

print(SPACEMAN[0])
play_again = True
while play_again:

    words_list = ['netherland', 'croatia', 'uzbekistan']
    chosen_word = random.choice(words_list).lower()
    guess = None
    # contains guessed letters
    guessed_letters = []
    blank_word = []

    for letter in chosen_word:
        blank_word.append('_')
    attempts = 6

    while attempts > 0:

        if attempts != 0 and '_' in blank_word:
            print(('\nYou have {} attempts left').format(attempts))
        try:
            guess = str(input('\nPlease select a letter between A-Z')).lower()
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
                continue
            else:
                pass
            
            guessed_letters.append(guess)

            if guess not in chosen_word:
                attempts -= 1
                print(SPACEMAN[(len(SPACEMAN) - 1) - attempts])

            else:
                search_more = True
                start_search_index = 0
                while search_more:
                    try:
                        # checking for double letters in the word 
                        found_at_index = chosen_word.index(guess, start_search_index)
                        blank_word[found_at_index] = guess
                        start_search_index = found_at_index + 1
                    except:
                        search_more = False

            print(''.join(blank_word))
            if attempts == 0:
                print(('GAME OVER! The word was {}').format(chosen_word))
                print('\nDo you want to play again? Type "Yes" or "y')
                response = input('>> ').lower()
                if response not in ['yes', 'y']:
                    play_again = False
                    print('Thanks for playing Spaceman!')
                break

            if '_' not in blank_word:
                print(('\nCongrats! {} was the hidden word').format(chosen_word))
                print('\nDo you want to play again? Type "Yes" or "y')
                response = input('>> ').lower()
                if response not in ['yes', 'y']:
                    play_again = False
                    print('Thanks for playing Spaceman!')
                break


                



