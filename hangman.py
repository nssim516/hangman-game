import random

# List of words and wrong letters used for the game
words = ["laptop", "computer", "coding", "console", "television", "phone"]
WrongLettersUsed = []


# Choosing a word for the round
def choose_word(words):
  return random.choice(words)


# Formatting the word to display that takes a word parameter and guesses amount
def display_word(word, guesses):
  display = ""
  for letter in word:
    if letter in guesses and guesses[letter]:
      display += letter
    else:
      display += "_"
  return display


# Formatting the hangman display that takes a parameter of wrong guesses
def display_hangman(wrong_guesses):
  if wrong_guesses == 0:
    print("  +---+")
    print("      |")
    print("      |")
    print("      |")
    print("      |")
    print("=========")
    print("Letters used: " + ", ".join(WrongLettersUsed))
  elif wrong_guesses == 1:
    print("  +---+")
    print("  O   |")
    print("      |")
    print("      |")
    print("      |")
    print("=========")
    print("Letters used: " + ", ".join(WrongLettersUsed))
  elif wrong_guesses == 2:
    print("  +---+")
    print("  O   |")
    print("  |   |")
    print("      |")
    print("      |")
    print("=========")
    print("Letters used: " + ", ".join(WrongLettersUsed))
  elif wrong_guesses == 3:
    print("  +---+")
    print("  O   |")
    print(" /|   |")
    print("      |")
    print("      |")
    print("=========")
    print("Letters used: " + ", ".join(WrongLettersUsed))
  elif wrong_guesses == 4:
    print("  +---+")
    print("  O   |")
    print(" /|\  |")
    print("      |")
    print("      |")
    print("=========")
    print("Letters used: " + ", ".join(WrongLettersUsed))
  elif wrong_guesses == 5:
    print("  +---+")
    print("  O   |")
    print(" /|\  |")
    print(" /    |")
    print("      |")
    print("=========")
    print("Letters used: " + ", ".join(WrongLettersUsed))
  else:
    print("  +---+")
    print("  O   |")
    print(" /|\  |")
    print(" / \  |")
    print("      |")
    print("=========")
    print("Letters used: " + ", ".join(WrongLettersUsed))


# Main game function
def play_hangman():
  word = choose_word(words)
  guesses = {}
  wrong_guesses = 0
  max_wrong_guesses = 6

  print("Welcome to Hangman!")
  while wrong_guesses < max_wrong_guesses:
    print(display_word(word, guesses))
    guess = input("Guess a letter: ").lower()

    if guess in guesses:
      print("You already guessed that letter.")
    elif guess in word:
      guesses[guess] = True
      print("\033[32mCorrect!\033[0m")
    else:
      wrong_guesses += 1
      guesses[guess] = False
      WrongLettersUsed.append(guess)
      print("\033[31mWrong!\033[0m")
      display_hangman(wrong_guesses)

    if "_" not in display_word(word, guesses):
      print("\033[32mYOU WIN!\033[0m")
      return

  print("\033[31mGame over! The word was: \033[0m", word)
  display_hangman(max_wrong_guesses)


# Calling of main game function
play_hangman()
