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